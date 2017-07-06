import ccircle
from math import *

window = ccircle.Window()
window.toggleMaximized()
window.hideMouse()

points = []

click = False
r = 0
g = 0
b = 0
s = 10

while window.isOpen():
    window.clear(1, 1, 1)
    mx, my = window.getMousePos()
    window.drawRect(10, 10, 50, 50, 1, 0, 0)

    if ccircle.isMouseDown('left'):
        points.append((mx, my, 100, r, g, b))


    for point in points:
        if ccircle.isMouseDown('left') == True:
            click = True
            if mx > 10 and mx < 60 and my > 10 and my < 60:
                if click == True:
                    r = 1
        window.drawCircle(point[0], point[1], 8, r, g, b)


    window.drawCircle(mx, my, 8, 0.1, 0.5, 0.1)
    window.update()