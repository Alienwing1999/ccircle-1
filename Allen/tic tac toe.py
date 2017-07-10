import ccircle

window = ccircle.Window("Tic Tac Toe", 800, 800)

down = False

click = 0

objects = []

'''

class O():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def drawO(self, x, y):
        window.drawCircle(x, y, 50, 1, 0, 0)
        window.drawCircle(x, y, 45, 1, 1, 1)

class X():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def drawX(self, x, y):
        window.drawLine(x - 25, y - 25, x + 25, y + 25, 20, 0, 0, 0)
        window.drawLine(x + 25, y - 25, x - 25, y + 25, 20, 0, 0, 0)

'''

while window.isOpen():
    window.clear(1, 1, 1)
    window.drawLine(300, 100, 300, 700, 20, 0, 0, 0)
    window.drawLine(500, 100, 500, 700, 20, 0, 0, 0)
    window.drawLine(100, 300, 700, 300, 20, 0, 0, 0)
    window.drawLine(100, 500, 700, 500, 20, 0, 0, 0)



    mx, my = window.getMousePos()

    if 100 < mx < 300:
        if 100 < my < 300:
            if ccircle.isMouseDown('left'):

                if click % 2 == 0:
                    O.drawO(O, 200, 200)
                    list.append(O(mx, my))
                    # click += 1

    window.update()
