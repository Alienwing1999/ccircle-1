import world
import ccircle
import random
import characters
import time



window = ccircle.Window('Naruto game', 1000, 800)
my_world = world.World('Naruto')
mx, my = window.getMousePos()

madara = ccircle.Image('madara.png')



image = ccircle.Image('map.jpg')

Madara = characters.Char(madara)
my_world.add(Madara)

start = time.time()
dt = 1.0 / 60.0

while window.isOpen():
    window.clear(0.1, 0.1, 0.1)

    image.draw(0, 0, 1000, 800)

    my_world.update(15 * dt, window)
    my_world.draw(window)

    window.update()

    now = time.time()
    dt = now - start
    start = now