import ccircle

class Char:
    def __init__(self, image):
        self.type = 'character'
        self.x = 500
        self.y = 400
        self.vx = 0
        self.vy = 0
        self.vx1 = 0
        self.vy1 = 0
        self.fx = 0
        self.fy = 0
        self.mass = 1
        self.fx1 = 0
        self.fy2 = 0
        self.im = image
        #self.rspeed = 0

    def apply_force(self, fx, fy):
        self.fx += fx
        self.fy += fy

    def draw(self, window):
        self.im.drawSub(self.x, self.y, 50, 70, 0, 30, 50, 70)

    def update(self, dt, window):

        mx, my = window.getMousePos()
        self.x += dt * self.vx
        self.y += dt * self.vy
        accel_y = self.fy / self.mass
        self.vy += dt * accel_y
        self.fx = 0
        self.fy = 0


        if self.y > 1000:
            self.vy *= 0

        if ccircle.isKeyDown('a'):
            self.vx = -20

        elif ccircle.isKeyDown('d'):
            self.vx = 20

        else:
            self.vx = 0

        if ccircle.isKeyDown('w'):
            self.vy = -20

        elif ccircle.isKeyDown('s'):
            self.vy = 20

        else:
            self.vy = 0

