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
            np[(x[24])] = (x[25],x[26],x[27])
            np[(x[28])] = (x[29],x[30],x[31])
            np[(x[32])] = (x[33],x[34],x[35])
            np[(x[36])] = (x[37],x[38],x[39])            
            np[(x[40])] = (x[41],x[42],x[43])
            np[(x[44])] = (x[45],x[46],x[47])
            np[(x[48])] = (x[49],x[50],x[51])
            np[(x[56])] = (x[57],x[58],x[59])
            np[(x[60])] = (x[61],x[62],x[63])            
            np[(x[64])] = (x[65],x[66],x[67])
            np[(x[68])] = (x[69],x[70],x[71])
            np[(x[72])] = (x[73],x[74],x[75])
            np[(x[76])] = (x[77],x[78],x[79])
            np[(x[80])] = (x[81],x[82],x[83])
            np[(x[84])]  = (x[85],x[86],x[87])
            np[(x[88])]  = (x[89],x[90],x[91])
            np[(x[92])]  = (x[93],x[94],x[95])
            np[(x[96])]  = (x[97],x[98],x[99])
            np[(x[100])] = (x[101],x[102],x[103])
            np[(x[124])] = (x[125],x[126],x[127])
            np[(x[128])] = (x[129],x[130],x[131])
            np[(x[132])] = (x[133],x[134],x[135])
            np[(x[136])] = (x[137],x[138],x[139])
            np[(x[140])] = (x[141],x[142],x[143])
            np[(x[144])] = (x[145],x[146],x[147])
            np[(x[148])] = (x[149],x[150],x[151])
            np[(x[156])] = (x[157],x[158],x[159])
            np[(x[160])] = (x[161],x[162],x[163])            
            np[(x[164])] = (x[165],x[166],x[167])
            np[(x[168])] = (x[169],x[170],x[171])
            np[(x[172])] = (x[173],x[174],x[175])
            np[(x[176])] = (x[177],x[178],x[179])
            np[(x[180])] = (x[181],x[182],x[183])            
            np[(x[184])]  = (x[185],x[186],x[187])
            np[(x[188])]  = (x[189],x[190],x[191])
            np[(x[192])]  = (x[193],x[194],x[195])
            np[(x[196])]  = (x[197],x[198],x[199])
           
            np.write()

            
            
            for i in range (0,60):
                np[i] = (0,0,0)
            np.write() 
            
        except Exception:
            print ('apagalo otto')
    
        
                

        
