""" Configuraciones para tira reactiva de audio LED """

from __future__ import print_function
from __future__ import division
import os

DEVICE = 'esp8266'
"""
Dispositivo utilizado para controlar la tira de LED. Debe ser 'pi', 'esp8266';

'esp8266' significa que está usando un módulo ESP8266 para controlar la tira de LED
y los comandos se enviarán al ESP8266 a través de WiFi.

'pi' significa que está utilizando una Raspberry Pi como una unidad independiente para procesar 
la entrada de audio y controlar la tira de LED directamente.

"""


if DEVICE == 'esp8266':
    UDP_IP = '192.168.137.11'
    """ Dirección IP de ESP8266. Debe coincidir con IP en main.py """
    UDP_PORT = 80
    """Número de puerto utilizado para la comunicación de socket entre Python y ESP8266"""
    SOFTWARE_GAMMA_CORRECTION = False
    """Se establece en False porque el firmware maneja la corrección de gamma y la interpolacion"""

if DEVICE == 'pi':
    LED_PIN = 18
    """Pin GPIO conectado a los píxeles de la tira de LED (debe ser compatible con PWM)"""
    LED_FREQ_HZ = 800000
    """Frecuencia de la señal LED en Hz (generalmente 800 kHz)"""
    LED_DMA = 5
    """Canal DMA utilizado para generar la señal PWM (prueba 5)"""
    BRIGHTNESS = 255
    """Brillo de la tira de LED entre 0 y 255"""
    LED_INVERT = True
    """Establecer True si se usa un convertidor inversor de nivel lógico"""
    SOFTWARE_GAMMA_CORRECTION = True
    """Se establece en True porque Raspberry Pi no utiliza la interpolación de hardware"""

if DEVICE == 'blinkstick':
    SOFTWARE_GAMMA_CORRECTION = True
    """Set to True because blinkstick doesn't use hardware dithering"""

USE_GUI = True
"""Se muestre o no un gráfico de visualización de la GUI de PyQtGraph"""

DISPLAY_FPS = True
"""Si se muestra el FPS cuando se ejecuta (puede reducir el rendimiento)"""

N_PIXELS = 50
"""Número de píxeles en la tira LED (debe coincidir con el firmware de ESP8266)"""

GAMMA_TABLE_PATH = os.path.join(os.path.dirname(__file__), 'gamma_table.npy')
"""Ubicación de la tabla de corrección gamma"""

MIC_RATE = 44100
"""Frecuencia de muestreo del micrófono en Hz"""

FPS = 60
"""Frecuencia de actualización deseada de la visualización (cuadros por segundo)

FPS indica la frecuencia de actualización deseada, o cuadros por segundo, de la
visualización de audio. La frecuencia de actualización real puede ser menor si la 
computadora no puede mantener con el valor FPS deseado.

Los cuadros de cuadros más altos mejoran la "capacidad de respuesta" y reducen la latencia del
La visualización, pero son más costosas computacionalmente.

Los cuadros de cuadros bajos son menos costosos computacionalmente, pero la visualización puede
aparece "lento" o desincronizado con el audio que se está reproduciendo si es demasiado bajo.

El FPS no debe exceder la tasa de actualización máxima de la tira LED, que
depende de la longitud de la tira LED.
"""
_max_led_FPS = int(((N_PIXELS * 30e-6) + 50e-6)**-1.0)
assert FPS <= _max_led_FPS, 'FPS debe ser <= {}'.format(_max_led_FPS)

MIN_FREQUENCY = 100

"""Las frecuencias por debajo de este valor se eliminarán durante el procesamiento de audio"""

MAX_FREQUENCY = 12000
"""Las frecuencias por encima de este valor se eliminarán durante el procesamiento de audio"""

N_FFT_BINS = 60
"""
Número de bandejas de frecuencia a usar cuando se transforma audio a dominio de frecuencia

Las transformaciones rápidas de Fourier se utilizan para transformar datos de audio de dominio de tiempo a
dominio de la frecuencia. Se asignan las frecuencias presentes en la señal de audio.
a sus respectivos contenedores de frecuencia. Este valor indica el número de
contenedores de frecuencia a utilizar.

Un pequeño número de contenedores reduce la resolución de frecuencia de la visualización.
pero mejora la resolución de amplitud. Lo contrario es cierto cuando se utiliza un gran
número de contenedores. ¡Más contenedores no siempre es mejor!
No tiene sentido usar más contenedores que píxeles en la tira de LED.
"""

N_ROLLING_HISTORY = 2
"""Número de tramas de audio pasadas para incluir en la ventana móvil"""

MIN_VOLUME_THRESHOLD = 1e-7
"""No se muestra la visualización de música si el volumen de audio grabado por debajo del umbral"""
