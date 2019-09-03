from machine import Pin
from neopixel import NeoPixel
import network
import socket
import time

pin = Pin(3, Pin.OUT)

np = NeoPixel(pin,60)


port=80
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('J-PC', 'jp123456')
while(wlan.isconnected() == False):
    time.sleep(1)
ip = wlan.ifconfig()[0]
print(ip)
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
s.bind((ip,port))
print('waiting....')
while True:
    x,addr=s.recvfrom(1024)  #s.sendto(data,addr)
    if x != b'':
        #x = data   
        try:
            np[(x[0])]  = (x[1],x[2],x[3]) 
            np[(x[4])]  = (x[5],x[6],x[7])
            np[(x[8])]  = (x[9],x[10],x[11])
            np[(x[12])] = (x[13],x[14],x[15])
            np[(x[16])] = (x[17],x[18],x[19])            
            np[(x[20])] = (x[21],x[22],x[23])
            
           
            np.write()

            
            
            for i in range (0,60):
                np[i] = (0,0,0)
            np.write() 
            
        except Exception:
            print ('apagalo otto')
    
        
                

        
