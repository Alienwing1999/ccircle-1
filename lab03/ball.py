import random

class Ball:
    def __init__(self, x, y):
        self.type = 'ball'
        self.x = x
        self.y = y
        self.vx = random.randint(-15, 15)
        self.vy = 0
        self.fx = 0
        self.fy = 0
        self.mass = 1
        self.rspeed = 0

    def apply_force(self, fx, fy):
        self.fx += fx
        self.fy += fy

    def draw(self, window):
        window.drawCircle(self.x, self.y, 16)

    def update(self, dt):
        self.x += dt * self.vx
        self.y += dt * self.vy
        accel_y = self.fy / self.mass
        self.vy += dt * accel_y
        self.fx = 0
        self.fy = 0

        if self.y > 500:
            self.vy *= -0.99
            self.y = 500

        if self.x > 800:
            self.x = 0
        if self.x < 0:
            self.x = 800