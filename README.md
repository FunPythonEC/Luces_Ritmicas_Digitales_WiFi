# Luces_Ritmicas_Digitales_WiFi

Luces rítmicas usando un esp8266/esp32 para controlar tiras led neopixel via WiFi con micropython y python.

## Descripción
Este repositorio contiene los scripts necesarios para correr el programa  de python en la computadora y hacer en analisis espectral del audio y tambien el script en micropython que debe ser grabado en el microcontrolador para controlar las tiras led.

En la carpeta python esta los scripts para el programa que analiza el audio y crea las ondas RGB que son enviadas via WiFi al microcontrolador.
En la carpeta micropython se encuentran las dos versiones del programa que recib ey decodifica los paquetes udp que son mostrados en los pixeles de las tiras rgb.

El proyecto original usaba ARDUINO pero decidi hacerlo con micrpython al inicio no habia encontrado la libreria en micropython adecauda para la decodificacion de los paquetes UDP asi que fue hecho casi manual por lo que el codigo crecia mucho y pasando los 50 pixeles se hacia muy tedioso, en la version 2 ya se hace soluciono este porblema y en un par de lineas decodifica los "bytes de colores" que llegan por WIFI, mejoró significativamente el rendimiento por lo que la vizualizacion de los efectos en las tiras RGB.


### Esquema con microcontrolador
![alt text](https://github.com/jhonpaulo98/Luces_Ritmicas_Digitales_WiFi/blob/master/imagenes/diagrama%20ESP.png)
### Esquema con Raspberry Pi
![alt text](https://github.com/jhonpaulo98/Luces_Ritmicas_Digitales_WiFi/blob/master/imagenes/diagrama%20raspberry-pi.png)

### Video demostrativo
<p align="center">
  <img width="640" height="480" src="https://github.com/jhonpaulo98/Luces_Ritmicas_Digitales_WiFi/blob/master/imagenes/demostracion.gif">
</p>

> <div style="padding:16px;">
> <div style="padding-top: 8px;">
> <div style=" color:#3897f0; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:550; line-height:18px;">Ver esta publicación en Instagram</div>
> </div>
> 
> [Una publicación compartida por Jhon Paulo (@jhon_p16)](https://www.instagram.com/p/Bpqj-FSh61d/?utm_source=ig_embed&utm_medium=loading) 
> publicada el <time style=" font-family:Arial,sans-serif; font-size:14px; line-height:17px;" datetime="2018-11-02T04:47:29+00:00">1 de Nov de 2018 a las 9:47 PDT</time> 
> </div>

