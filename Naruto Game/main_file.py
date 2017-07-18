import world
import ccircle
import random
import Ma
import time
import Ki

window = ccircle.Window('Naruto game', 1000, 800)
my_world = world.World('Naruto')
mx, my = window.getMousePos()

image = ccircle.Image('map.jpg')



#Madara

madara = ccircle.Image('madara_no_b.png')
madaraf = ccircle.Image('madaraf_no_b.png')

Madara = Ma.Char(madara, madaraf)
my_world.add(Madara)

'''#Kisame

kisame = ccircle.Image('kisame_no_b.png')
kisamef = ccircle.Image('kisamef_no_b.png')



Kisame = Ki.Char(kisame, kisamef)
my_world.add(Kisame)

'''

start = time.time()
dt = 1.0 / 60.0

while window.isOpen():
    window.clear(0.1, 0.1, 0.1)

    image.draw(0, 0, 1000, 800)

    my_world.update(5 * dt, window)
    my_world.draw(window)

    for i in my_world.objects:
        if i.type == 'character':
            i.apply_force(0, 45)

    window.update()

    now = time.time()
    dt = now - start
    start = now