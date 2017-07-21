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

Ki_lives = 3
Ma_lives = 3

image = ccircle.Image('map.jpg')

loading_screen = ccircle.Image('loading_screenf.png')

counter = 0

over = 0

heart = ccircle.Image('heartf.png')

#Madara

madara = ccircle.Image('madara_no_b.png')
madaraf = ccircle.Image('madaraf_no_b.png')

Madara = Ma.Char(madara, madaraf, my_world, Ma_lives)
my_world.add(Madara)

#Kisame

kisame = ccircle.Image('kisame_no_b.png')
kisamef = ccircle.Image('kisamef_no_b.png')



Kisame = Ki.Char(kisame, kisamef, my_world, Ki_lives)
my_world.add(Kisame)



start = time.time()
dt = 1.0 / 60.0

while window.isOpen():
    window.clear(0.1, 0.1, 0.1)

    if page == 0:


        loading_screen.draw(0, 0, 1200, 800)

        if counter < 150:
            font.draw("Press s to start", 389, 700, 20, 0, 0, 0)

        counter += 1
        if ccircle.wasKeyPressed('s'):
            page = 1
        if counter > 300:
            counter = 0

    if page == 1:
        image.draw(0, 0, 1200, 800)
        font.draw("Kisame (Player 1):", 20, 50)
        font.draw("Madara (Player 2):", 940, 50)

        for obj in my_world.objects:
            window.drawRect(obj.x + 10, obj.y - 20, obj.health/2, 5, 1, 0, 0)
            if obj.y > 800:
                obj.health = 0

        for i in range(len(my_world.objects)):
            if i < len(my_world.objects) and my_world.objects[i].health == 0:
                my_world.objects[i].lives -= 1
                del my_world.objects[i]
                counter = 0


        if Ki_lives == 3:
            heart.draw(50, 80, 30, 30)
            heart.draw(100, 80, 30, 30)
            heart.draw(150, 80, 30, 30)
        if Ki_lives == 2:
            heart.draw(50, 80, 30, 30)
            heart.draw(100, 80, 30, 30)
        if Ki_lives == 1:
            heart.draw(50, 80, 30, 30)

        if Ma_lives == 3:
            heart.draw(980, 80, 30, 30)
            heart.draw(1030, 80, 30, 30)
            heart.draw(1080, 80, 30, 30)
        if Ma_lives == 2:
            heart.draw(980, 80, 30, 30)
            heart.draw(1030, 80, 30, 30)

        if Ma_lives == 1:
            heart.draw(980, 80, 30, 30)


        if counter == 100:
            if len(my_world.objects) == 1 and my_world.objects[0].respawn == 'Ma':
                Ki_lives -= 1
                Kisame = Ki.Char(kisame, kisamef, my_world, Ki_lives)
                my_world.objects.append(Kisame)

            elif len(my_world.objects) == 1 and my_world.objects[0].respawn == 'Ki':
                Ma_lives -= 1
                Madara = Ma.Char(madara, madaraf, my_world, Ma_lives)
                my_world.objects.append(Madara)

        print(Ma_lives)

        if Ma_lives == 0:
            Ma_lives = 3
            page = 2
            over = 1




        if Ki_lives == 0:
            Ki_lives = 3
            page = 2
            over = 2




        for i in my_world.objects:
            if i.type == 'character':
                i.apply_force(0, 45)
        mx, my = window.getMousePos()
        counter += 1
        my_world.update(5 * dt, window)
        my_world.draw(window)
    if page == 2:
        Ma_lives = 3
        Ki_lives = 3
        image.draw(0, 0, 1200, 800)
        font.draw("Game over", 150, 200, 80, 1, 0, 0)
        if over == 1:
            font.draw("Player 2 wins!", 430, 340, 20, 0, 0, 0)
        if over == 2:
            font.draw("Player 1 wins!", 430, 340, 20, 0, 0, 0)
        font.draw("Press r to restart", 400, 600, 20, 1, 1, 1)

        if ccircle.wasKeyPressed('r'):
            page = 0

    for object in my_world.objects:
        if object.respawn == 'Ma': print(object.lives)

    window.update()

    now = time.time()
    dt = now - start
    start = now