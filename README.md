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

For a full post with more details go to: https://ogreden.net/talking-halloween-pumpkin/


You don't have to use the same hardware or even the same kind of LEDs that I used but just for reference...
Hardware I used:

Raspberry pi 2 b+
Raspberry pi pico w
Adafruit Mono 2.5W Class D Audio Amplifier - PAM8302 (Just cuz I had it on hand)
A tiny 8ohm 1 watt speaker (Also just cuz I had it on hand)
Generic PIR sensor
WS2812B addressable LEDs

I powered the 2 boards seperate out of laziness and to avoid any kind of amp issues.

The Pi Pico was powered by 2 recycled Juul lipos.
The Pi2b was powered with a generic usb power bank.

