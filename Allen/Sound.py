import ccircle
from math import *
import time
import random


window = ccircle.Window('Lab: Audio Synthesis')
mysound = ccircle.Sound()

def sawtooth(t,f):
    return 2.0 * ((t*f)%1.0)-1.0

def sine(t,f):
        return sin(10.0 * pi * t * f)




for i in range(44100):
    t = i / 44100
    mysound.addSample(sine(t, 120))
mysound.play()
time.sleep(1)
