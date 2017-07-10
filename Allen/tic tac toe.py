# figure out how to detect the change in the mouse being clicked
# try to do this with objects instead

import ccircle

window = ccircle.Window("Tic Tac Toe", 800, 800)

down = False

click = 0

list = [0, 0, 0, 0, 0, 0, 0, 0, 0]

while window.isOpen():
    window.clear(1, 1, 1)
    window.drawLine(300, 100, 300, 700, 20, 0, 0, 0)
    window.drawLine(500, 100, 500, 700, 20, 0, 0, 0)
    window.drawLine(100, 300, 700, 300, 20, 0, 0, 0)
    window.drawLine(100, 500, 700, 500, 20, 0, 0, 0)

'''    
    
    mx, my = window.getMousePos()

    a = ccircle.isMouseDown('left')

    if 100 < mx < 300:
        if 100 < my < 300:
            if a is False:
                list[0] = 1
                click += 1

        if 300 < my < 500:
            if a is False:
                list[1] = 1
                click += 1
        if 500 < my < 700:
            if a is False:
                list[2] = 1
                click += 1
    if 300 < mx < 500:
        if 100 < my < 300:
            if a is False:
                list[3] = 1
                click += 1
        if 300 < my < 500:
            if a is False:
                list[4] = 1
                click += 1
        if 500 < my < 700:
            if a is False:
                list[5] = 1
                click += 1
    if 500 < mx < 700:
        if 100 < my < 300:
            if a is False:
                list[6] = 1
                click += 1
        if 300 < my < 500:
            if a is False:
                list[7] = 1
                click += 1
        if 500 < my < 700:
            if a is False:
                list[8] = 1
                click += 1
    if click % 2 == 0:
        if list[0] == 1:
            window.drawCircle(200, 200, 50, 1, 0, 0)
            window.drawCircle(200, 200, 45, 1, 1, 1)
        if list[1] == 1:
            window.drawCircle(200, 400, 50, 1, 0, 0)
            window.drawCircle(200, 400, 45, 1, 1, 1)
        if list[2] == 1:
            window.drawCircle(200, 600, 50, 1, 0, 0)
            window.drawCircle(200, 600, 45, 1, 1, 1)
        if list[3] == 1:
            window.drawCircle(400, 200, 50, 1, 0, 0)
            window.drawCircle(400, 200, 45, 1, 1, 1)
        if list[4] == 1:
            window.drawCircle(400, 400, 50, 1, 0, 0)
            window.drawCircle(400, 400, 45, 1, 1, 1)
        if list[5] == 1:
            window.drawCircle(400, 600, 50, 1, 0, 0)
            window.drawCircle(400, 600, 45, 1, 1, 1)
        if list[6] == 1:
            window.drawCircle(600, 200, 50, 1, 0, 0)
            window.drawCircle(600, 200, 45, 1, 1, 1)
        if list[7] == 1:
            window.drawCircle(600, 400, 50, 1, 0, 0)
            window.drawCircle(600, 400, 45, 1, 1, 1)
        if list[8] == 1:
            window.drawCircle(600, 600, 50, 1, 0, 0)
            window.drawCircle(600, 600, 45, 1, 1, 1)
    else:
        if list[0] == 1:
            window.drawLine(200 - 25, 200 - 25, 200 + 25, 200 + 25, 20, 0, 0, 0)
            window.drawLine(200 + 25, 200 - 25, 200 - 25, 200 + 25, 20, 0, 0, 0)

        if list[1] == 1:
            window.drawLine(200 - 25, 400 - 25, 200 + 25, 400 + 25, 20, 0, 0, 0)
            window.drawLine(200 + 25, 400 - 25, 200 - 25, 400 + 25, 20, 0, 0, 0)

        if list[2] == 1:
            window.drawLine(200 - 25, 600 - 25, 200 + 25, 600 + 25, 20, 0, 0, 0)
            window.drawLine(200 + 25, 600 - 25, 200 - 25, 600 + 25, 20, 0, 0, 0)

        if list[3] == 1:
            window.drawLine(400 - 25, 200 - 25, 400 + 25, 200 + 25, 20, 0, 0, 0)
            window.drawLine(400 + 25, 200 - 25, 400 - 25, 200 + 25, 20, 0, 0, 0)

        if list[4] == 1:
            window.drawLine(400 - 25, 400 - 25, 400 + 25, 400 + 25, 20, 0, 0, 0)
            window.drawLine(400 + 25, 400 - 25, 400 - 25, 400 + 25, 20, 0, 0, 0)

        if list[5] == 1:
            window.drawLine(400 - 25, 600 - 25, 400 + 25, 600 + 25, 20, 0, 0, 0)
            window.drawLine(400 + 25, 600 - 25, 400 - 25, 600 + 25, 20, 0, 0, 0)

        if list[6] == 1:
            window.drawLine(600 - 25, 200 - 25, 600 + 25, 200 + 25, 20, 0, 0, 0)
            window.drawLine(600 + 25, 200 - 25, 600 - 25, 200 + 25, 20, 0, 0, 0)

        if list[7] == 1:
            window.drawLine(600 - 25, 400 - 25, 600 + 25, 400 + 25, 20, 0, 0, 0)
            window.drawLine(600 + 25, 400 - 25, 600 - 25, 400 + 25, 20, 0, 0, 0)

        if list[8] == 1:
            window.drawLine(600 - 25, 600 - 25, 600 + 25, 600 + 25, 20, 0, 0, 0)
            window.drawLine(600 + 25, 600 - 25, 600 - 25, 600 + 25, 20, 0, 0, 0)
'''

    class O:
        def __init__(self):

    window.update()

