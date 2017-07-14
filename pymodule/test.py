import os
d = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.append(d + '\\dist')

import ccircle
import random
import time
from math import *

window = ccircle.Window('CCircle Module Test', 800, 800)
cat = ccircle.Image('res/cat.png')
font = ccircle.Font('res/FiraMono.ttf')

sound = ccircle.Sound()
sound.addSine(0, 1, 440, 0.5)
sound.addSine(0.5, 0.5, 880, 0.5)
sound.play()

while window.isOpen():
  window.clear(0.1, 0.1, 0.1)
  mx, my = window.getMousePos()
  window.drawPoint(mx, my, 8)

  cat.draw(16, 16, 128, 128)
  font.draw("I'm a cat! :3", 140, 64 + 32, 12)

  window.update()
