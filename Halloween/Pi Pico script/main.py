from machine import Pin
from machine import UART
import time
import neopixel
import os


uart = UART(0, 115200)

b = None
msg = ''
FORMAT = 'utf-8' #format to decode from bytes to string
HoldTime = 0.075 #length of time in seconds for how long led stays bright

Num_Led = 14 #number of our adressable leds
Led_Pin = Pin(12, Pin.OUT)
Pixels = neopixel.NeoPixel(Led_Pin, Num_Led)

FullBright = (60,20,180)
Dim = (20, 10, 50)

Pixels.fill(Dim)
Pixels.write()

def main():
    msg = ''
    while True:
        #if the uart pin (gpio 0) reads any data, decode it and if its == '1', blinky time
        if uart.any():
            b = uart.readline()
            try:
                msg = b.decode(FORMAT)
                print(msg)
            except:
                pass
        if msg == '1':
            Pixels.fill(FullBright)
            Pixels.write()
            time.sleep(HoldTime)
            Pixels.fill(Dim)
            Pixels.write()
    
if __name__ == '__main__':
    main()
    
    