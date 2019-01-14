from __future__ import print_function
from __future__ import division

import platform
import numpy as np
import config

# ESP8266 usa comunicación WiFi
if config.DEVICE == 'esp8266':
    import socket
    _sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Raspberry Pi controla la tira LED directamente
elif config.DEVICE == 'pi':
    import neopixel
    strip = neopixel.Adafruit_NeoPixel(config.N_PIXELS, config.LED_PIN,
                                       config.LED_FREQ_HZ, config.LED_DMA,
                                       config.LED_INVERT, config.BRIGHTNESS)
    strip.begin()
elif config.DEVICE == 'blinkstick':
    from blinkstick import blinkstick
    import signal
    import sys
    #Apaga todos los leds cuando se invoca.
    def signal_handler(signal, frame):
        all_off = [0]*(config.N_PIXELS*3)
        stick.set_led_data(0, all_off)
        sys.exit(0)

    stick = blinkstick.find_first()
    # Crea un oyente que apague los leds cuando el programa termine.
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

_gamma = np.load(config.GAMMA_TABLE_PATH)
"""Tabla de búsqueda gamma utilizada para la corrección de brillo no lineal"""

_prev_pixels = np.tile(253, (3, config.N_PIXELS))
"""Los valores de píxeles que se mostraron más recientemente en la tira LED"""

pixels = np.tile(1, (3, config.N_PIXELS))
"""Valores de píxel para la tira de LED"""

_is_python_2 = int(platform.python_version_tuple()[0]) == 2

def _update_esp8266():
    """
    Envía paquetes UDP a ESP8266 para actualizar los valores de la tira LED
    
    El ESP8266 recibirá y decodificará los paquetes para determinar qué valores
    para mostrar en la tira LED. El protocolo de comunicación soporta tiras de LED.
    Con un máximo de 256 LEDs.

    El esquema de codificación de paquetes es:
        | i | r | g | b |
    dónde
        i (0 a 255): índice del LED para cambiar (primer led empieza en cero)
        r (0 a 255): valor r - red/rojo de LED
        g (0 a 255): valor g - green/verde de LED
        b (0 a 255): valor b - blue/azul del LED
    """
    global pixels, _prev_pixels
    # Truncar valores y convertir a entero
    pixels = np.clip(pixels, 0, 255).astype(int)
    # Opcionalmente aplicar la corrección gamma.
    p = _gamma[pixels] if config.SOFTWARE_GAMMA_CORRECTION else np.copy(pixels)
    MAX_PIXELS_PER_PACKET = 126
    # Índices de pixel
    idx = range(pixels.shape[1])
    idx = [i for i in idx if not np.array_equal(p[:, i], _prev_pixels[:, i])]
    n_packets = len(idx) // MAX_PIXELS_PER_PACKET + 1
    idx = np.array_split(idx, n_packets)
    for packet_indices in idx:
        m = '' if _is_python_2 else []
        for i in packet_indices:
            if _is_python_2:
                m += chr(i) + chr(p[0][i]) + chr(p[1][i]) + chr(p[2][i])
            else:
                m.append(i)        # Índice de píxeles para cambiar
                m.append(p[0][i])  # Valor de píxel (R red) rojo 
                m.append(p[1][i])  # Valor de píxel (G green) verde
                m.append(p[2][i])  # Valor de píxel (B blue) azul
        m = m if _is_python_2 else bytes(m)
        _sock.sendto(m, (config.UDP_IP, config.UDP_PORT))
    _prev_pixels = np.copy(p)


def _update_pi():
    """Escribe nuevos valores de LED en la tira de LED de Raspberry Pi

    Raspberry Pi utiliza el rpi_ws281x para controlar la tira de LED directamente.
    Esta función actualiza la tira de LED con nuevos valores.
    """
    global pixels, _prev_pixels
    # Truncar valores y convertir a entero
    pixels = np.clip(pixels, 0, 255).astype(int)
    # Corrección gamma opcional
    p = _gamma[pixels] if config.SOFTWARE_GAMMA_CORRECTION else np.copy(pixels)
    # Codificar valores de LED de 24 bits en enteros de 32 bits
    r = np.left_shift(p[0][:].astype(int), 8)
    g = np.left_shift(p[1][:].astype(int), 16)
    b = p[2][:].astype(int)
    rgb = np.bitwise_or(np.bitwise_or(r, g), b)
    # Update the pixels
    for i in range(config.N_PIXELS):
        # Ignorar píxeles si no han cambiado (ahorra ancho de banda)
        if np.array_equal(p[:, i], _prev_pixels[:, i]):
            continue
        strip._led_data[i] = rgb[i]
    _prev_pixels = np.copy(p)
    strip.show()

def _update_blinkstick():
    """ Escribe nuevos valores de LED en el Blinkstick.
        Esta función actualiza la tira de LED con nuevos valores.
    """
    global pixels
    
    # Truncar valores y convertir a entero
    pixels = np.clip(pixels, 0, 255).astype(int)
    # Optional gamma correction
    p = _gamma[pixels] if config.SOFTWARE_GAMMA_CORRECTION else np.copy(pixels)
    # Leer los valores rgb
    r = p[0][:].astype(int)
    g = p[1][:].astype(int)
    b = p[2][:].astype(int)

    #Creamos un array en el que almacenaremos los estados led.
    newstrip = [None]*(config.N_PIXELS*3)

    for i in range(config.N_PIXELS):
        # blinkstick usa formato GRB (green, red, blue)/(verde, rojo, azul)
        newstrip[i*3] = g[i]
        newstrip[i*3+1] = r[i]
        newstrip[i*3+2] = b[i]
    #enviar los datos al blinkstick
    stick.set_led_data(0, newstrip)


def update():
    """Actualiza los valores de la tira de LED"""
    if config.DEVICE == 'esp8266':
        _update_esp8266()
    elif config.DEVICE == 'pi':
        _update_pi()
    elif config.DEVICE == 'blinkstick':
        _update_blinkstick()
    else:
        raise ValueError('Dispositivo no válido seleccionado')


# Ejecutar este archivo para ejecutar una prueba de filamento de LED
# Si todo funciona, debería ver un desplazamiento de píxeles rojo, verde y azul
# a través de la tira de LED continuamente
if __name__ == '__main__':
    import time
    # Turn all pixels off
    pixels *= 0
    pixels[0, 0] = 255  # Establecer el primer píxel rojo
    pixels[1, 1] = 255  # Establecer segundo píxel verde
    pixels[2, 2] = 255  # Establecer 3er píxel azul
    print('Comenzando prueba de tira LED')
    while True:
        pixels = np.roll(pixels, 1, axis=1)
        update()
        time.sleep(.1)
