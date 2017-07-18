import ccircle



class Char:
    def __init__(self, image, image2):
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
        self.im2 = image2
        self.a = 0

        #self.rspeed = 0

    def apply_force(self, fx, fy):
        self.fx += fx
        self.fy += fy

    def draw(self, window):
        if ccircle.isKeyDown('a'):
            self.vx = -20
            self.im2.drawSub(self.x, self.y, 60, 82, 968, 184, 70, 90)
            self.a = 1

        elif ccircle.isKeyDown('d'):
            self.vx = 20
            self.im.drawSub(self.x, self.y, 60, 82, 14, 184, 70, 90)
            self.a = 2
        else:
            if self.a == 1:
                self.im2.drawSub(self.x, self.y, 60, 82, 968, 184, 70, 90)
            else:
                self.im.drawSub(self.x, self.y, 60, 82, 14, 184, 70, 90)




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

        if self.y > 380:
            self.y = 380
            self.vy = 0



        else:
            self.vx = 0

        if ccircle.isKeyDown('w'):
            self.vy = -110

        if self.y < -150:
            self.y = -150
            self.vy = 0





