import world
import ccircle
import random
import Ma
import time
import Ki


window = ccircle.Window('Naruto game', 1200, 800)
my_world = world.World('Naruto')

font = ccircle.Font('FiraMono.ttf')

page = 0

image = ccircle.Image('map.jpg')

loading_screen = ccircle.Image('loading_screenf.png')

counter = 0

#Madara

madara = ccircle.Image('madara_no_b.png')
madaraf = ccircle.Image('madaraf_no_b.png')

Madara = Ma.Char(madara, madaraf, my_world)
my_world.add(Madara)

#Kisame

kisame = ccircle.Image('kisame_no_b.png')
kisamef = ccircle.Image('kisamef_no_b.png')



Kisame = Ki.Char(kisame, kisamef, my_world)
my_world.add(Kisame)



start = time.time()
dt = 1.0 / 60.0

while window.isOpen():
    window.clear(0.1, 0.1, 0.1)
    if page == 0:

        loading_screen.draw(0, 0, 1200, 800)

        if counter < 100:
            font.draw("Press s to start", 389, 700, 20, 0, 0, 0)

        counter += 1
        if ccircle.isKeyDown('s'):
            page = 1
        if counter > 200:
            counter = 0

    elif page == 1:
        image.draw(0, 0, 1200, 800)
        font.draw("Kisame:", 20, 50)

        for i in range(len(my_world.objects)):
            if my_world.objects[i].health < 0:
                del my_world.objects[i]
                counter = 0
        if counter == 100:
            my_world.objects.append(Ki.Char(kisame, kisamef, my_world))





        my_world.update(5 * dt, window)
        my_world.draw(window)

        window.drawRect(Kisame.x + 10, Kisame.y - 20, Kisame.health/2, 5, 1, 0, 0)
        window.drawRect(Madara.x + 10, Madara.y - 20, Madara.health / 2, 5, 1, 0, 0)

        for i in my_world.objects:
            if i.type == 'character':
                i.apply_force(0, 45)
        mx, my = window.getMousePos()
        counter += 1

    window.update()

    now = time.time()
    dt = now - start
    start = now