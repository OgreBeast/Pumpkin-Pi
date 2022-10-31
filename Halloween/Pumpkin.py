import time
import RPi.GPIO as io
import pygame
import json
from pathlib import Path
import random
import os
import serial

#serial
ser = serial.Serial(
        port='/dev/ttyAMA0',
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=60
        )

FORMAT = 'utf-8'

pygame.mixer.init()

#Pin setup
io.setmode(io.BCM)
io.setwarnings(False)

PIR = 4

io.setup(PIR, io.IN, io.PUD_DOWN) #Set to pull down, thats important

#Audio setup
AudioPath = Path.cwd() / 'AudioFiles/'

SpookPathList = list(AudioPath.rglob('*.wav'))

SpookList = []

#creating the list of all the wav file paths
for w in SpookPathList:
    SpookList.append(os.path.basename(w))

print(SpookList)

CurrentWavPath = str(random.choice(SpookPathList))
CurrentWavName = os.path.basename(CurrentWavPath)
pygame.mixer.music.load(CurrentWavPath)

# LEDS
Num_Led = 29

#json stuff
Jsonpath = Path.cwd() / 'JSON/'
JsonFilePath = str(Jsonpath) + '/WavTimings.json'

WavTimings = {}

#load json timing data
with open(str(JsonFilePath), 'r') as file:
    WavTimings = json.load(file)

StartTime = time.time()

while True:
    #if the motion sensor detects something
    if io.input(PIR) == 1:
        MyTimer = 0
        print('I see you')        
        pygame.mixer.music.play() #play randomly selected clip
        StartTime = time.time() #update start time
        #while the auido file is playing
        while pygame.mixer.music.get_busy() == True:
            #loop through all the wave timings for that wav file
            for timing in WavTimings[CurrentWavName]:
                MyTimer = 0
                #while a timer is less than the timing of the json data
                while MyTimer < timing:
                    MyTimer = time.time() - StartTime #update mytimer
                
                #Write '1' to serial buffer
                ser.write('1'.encode(FORMAT))
                time.sleep(0.05) #wait a small amount of time to help avoid sending a '1' and '0' in the same buffer
                ser.write('0'.encode(FORMAT))
                
        time.sleep(0.1) 
        CurrentWavPath = str(random.choice(SpookPathList)) #choose a random new wav file
        CurrentWavName = os.path.basename(CurrentWavPath) #get its name
        print('Next file: ', CurrentWavName) 
        time.sleep(0.5) # wait here to attempt to avoid an overrun error
        pygame.mixer.music.load(CurrentWavPath) #load up the next wav in pygame mixer

