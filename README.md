# Pumpkin-Pi
Blinking talking pumpkin thingie I made.


How to use the code:

Pumpkin.py is the main program file.  It will search through the audio files and randomly play them if the PIR (motion detector) is triggered.
Put some .wav files in the audio files folder and run 'WavSpectrum.py' to look at them and determine some good timings.  It will spit out a json file in the JSON folder.  

Now you can run Pumpkin.py and hopefully it will work.  Depending on your wav files you will have to adjust 2 variables in WavSpectrum.py to get some
timings that you like.  

Change:
MIN_TIME_GAP = 0.18
AMP_PEAK = 12000

For a full post with more details go to: 
