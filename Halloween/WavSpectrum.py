import sys
from tkinter import W
import wave
import numpy as np
import warnings
import json
import os
from pathlib import Path

#stupid crap about stuff
warnings.filterwarnings("ignore")

WavTimes = {}
Clips = []
Dirpath = Path.cwd() / 'JSON/'

#Most important variables here, tweak these until you get a good looking blink timing
MIN_TIME_GAP = 0.18
AMP_PEAK = 12000 #Should not go above like 32000

PrevTime = 0
AudioPath = 'AudioFiles/'
Jsonpath = Path.cwd() / 'JSON/WavTimings.json'

def main():
    path = Path.cwd() / AudioPath

    #grab all the files with '.wav' extension    
    for c in list(path.rglob('*wav')):
        Clips.append(os.path.basename(c))

    #make a JSON folder if it doesn't exist
    if Dirpath.exists() == False:
       Dirpath.mkdir()

    ExportJSONTimings(Clips)

def ExportJSONTimings(ClipNames):
    #for every clip in the list, read the spectrum, and check against the thresholds
    for ClipName in ClipNames: 
        SignalTime = []
        PrevTime = 0
        WavPath = str(Path.cwd() / AudioPath / ClipName)
        
        #complicated bit of code that I got from stackoverflow
        #reads the spectrum and formats the time variable correctly
        spf = wave.open(WavPath, "r")
        signal = spf.readframes(-1)
        signal = np.fromstring(signal, "Int16")
        fs = spf.getframerate()
        Time = np.linspace(0, len(signal)/fs, num=len(signal))
        
        WavTimes[ClipName] = [] #initialize the dictionary entry as a list

        #loop through the spectrum and if you find a high amp peak, take note of the time
        #and don't grab another time until MIN_TIME_GAP as passed in the file duration
        for i in range(len(signal)):
            if signal[i] > AMP_PEAK and (abs(PrevTime - Time[i]) > MIN_TIME_GAP):
                SignalTime.append(Time[i])
                PrevTime = Time[i]

        #for all the timings found, round em to 1 decimal place and put em in a nice list 
        for k in range(len(SignalTime)):
            WavTimes[ClipName].append(round(SignalTime[k], 1))

        # write the timing data to a 'WavTimings.json' json file in the 'JSON' directory
        with open(str(Jsonpath), 'w') as file:
            json.dump(WavTimes, file)

main()

