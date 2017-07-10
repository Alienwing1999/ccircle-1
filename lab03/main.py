import ccircle
import world
import cloud
import random
import time
#import pokemon
import ball

window = ccircle.Window('Lab 4', 800, 600)
my_world = world.World('blah')
print(dir(my_world))

for i in range(200):
    x = random.randint(0, 800)
    y = random.randint(0, 150)
    size = 25 + 75 * (random.uniform(0,1) ** 2)
    vx = random.uniform(0,100)
    my_world.add(cloud.Cloud(x, y, size, vx))

'''

for i in range(5):
    x = random.randint(0, 800)
    y = random.randint(500, 600)
    my_world.add(pokemon.Pokemon(x, y))
    
'''
my_ball = ball.Ball(400, 300)
my_world.add(my_ball)

start = time.time()
dt = 1.0 / 60.0

while window.isOpen():
    window.clear(0.1, 0.1, 0.1)
    my_ball.apply_force(10, 9.8)
    my_world.update(5 * dt)
    my_world.draw(window)
    window.update()

    now = time.time()
    dt = now - start
    start = now
