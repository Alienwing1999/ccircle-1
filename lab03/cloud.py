class Cloud:
    def __init__(self, x, y, size, vx):
        self.x = x
        self.y = y
        self.vx = vx
        self.size = size

    def draw(self, window):
        window.drawCircle(self.x, self.y, self.size, 1, 1, 1, 0.25)

    def update(self, dt):
        self.x += dt * self.vx
        if self.x > 800:
            self.x = 0
        if self.x < 0:
            self.x = 800