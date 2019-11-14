from machine import Pin
from neopixel import NeoPixel
import network
import socket
import time
import utime

# número del pin digital
PIN=
# numero de leds en la tira
NLEDS=
#nombre de la red WiFi
SSID=
#contraseña de la red WiFi
PASSWD=

pin = Pin(PIN, Pin.OUT)
np = NeoPixel(pin,NLEDS)

port=80
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('SSID', 'PASSW')
while(wlan.isconnected() == False):
    time.sleep(1)
ip = wlan.ifconfig()[0]
print(ip)
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
s.bind((ip,port))
print('esperando datos....')
while True:
    
    x,addr=s.recvfrom(200)  #s.sendto(data,addr)
    
    if x != b'': 
            x=list(x)
            i=0
            ini=utime.ticks_us()
            for m in range(0,int(len(x)/4)):
                try:
                    np[x[i]]=(x[i+1],x[i+2],x[i+3])
                                       
                except Exception as e:
                    print(e)
                i+=4
            print(utime.ticks_diff(ini,utime.ticks_us()))
            np.write()       
            
            #s.close()
    




            
                

        
