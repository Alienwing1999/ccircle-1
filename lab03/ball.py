import random
import ccircle

class Ball:
    def __init__(self, x, y):
        self.type = 'ball'
        self.x = x
        self.y = y
        self.vx = random.randint(-15, 15)
        self.vy = 0
        self.vx1 = 0
        self.vy1 = 0
        self.fx = 0
        self.fy = 0
        self.mass = 1
        self.fx1 = 0
        self.fy2 = 0
        #self.rspeed = 0

    def apply_force(self, fx, fy):
        self.fx += fx
        self.fy += fy

    def draw(self, window):
        window.drawCircle(self.x, self.y, 16)

    def update(self, dt, window):

        mx, my = window.getMousePos()
        self.x += dt * self.vx
        self.y += dt * self.vy
        accel_y = self.fy / self.mass
        self.vy += dt * accel_y
        self.fx = 0
        self.fy = 0
        if abs(self.x - mx) < 25 and abs(self.fy - my) < 25:
            a = self.x - mx
            b = self.y - my
            self.x += dt * self.vx1
            self.y += dt * self.vy1
            accel_x1 = a / self.mass
            accel_y1 = b / self.mass
            self.vx1 += dt * accel_x1
            self.vy1 += dt * accel_y1

        if self.y > 500:
            self.y = 500
            self.vy *= -1.0


        if self.x > 800 or self.x < 0:
            self.vx = -self.vx

