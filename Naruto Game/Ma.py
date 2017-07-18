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
        self.ImageIndex = 0
        self.jump = 0

        #self.rspeed = 0

    def apply_force(self, fx, fy):
        self.fx += fx
        self.fy += fy

    def draw(self, window):


        if ccircle.isKeyDown('w'):
            if self.a == 2:
                if self.ImageIndex < 5:
                    self.im.drawSub(self.x-6, self.y-2, 70, 86, 0, 323, 53, 80)

                elif self.ImageIndex < 10:
                    self.im.drawSub(self.x, self.y, 70, 82, 53, 323, 53, 80)

                else:
                    self.im.drawSub(self.x, self.y, 70, 82, 106, 312, 53, 80)

                self.ImageIndex += 1

                if ccircle.isKeyDown('a'):
                    self.vx = -30
                    self.a = 1
                if ccircle.isKeyDown('d'):
                    self.vx = 30
                    self.a = 2

            else:
                if self.ImageIndex < 5:
                    print('a')
                    self.im2.drawSub(self.x+6, self.y+2, 70, 86, 922, 323, 53, 80)

                elif self.ImageIndex < 10:
                    print('b')
                    self.im2.drawSub(self.x, self.y, 70, 82, 869, 323, 53, 80)

                else:
                    print('c')
                    self.im2.drawSub(self.x, self.y, 70, 82, 816, 312, 53, 80)
                if ccircle.isKeyDown('a'):
                    self.vx = -30
                    self.a = 1
                if ccircle.isKeyDown('d'):
                    self.vx = 30
                    self.a = 2
                self.ImageIndex += 1
            if self.jump == 0:
                self.vy = -100
                self.jump += 1

        elif ccircle.isKeyDown('a'):
            self.vx = -30

            if self.ImageIndex < 50:
                self.im2.drawSub(self.x, self.y, 64, 82, 911, 224, 64, 65)

            elif self.ImageIndex < 100:
                self.im2.drawSub(self.x , self.y, 49, 82, 860, 224, 47, 65)

            elif self.ImageIndex < 150:
                self.im2.drawSub(self.x + 5, self.y, 52, 82, 810, 224, 52, 65)

            elif self.ImageIndex < 200:
                self.im2.drawSub(self.x, self.y, 66, 82, 742, 224, 64, 65)

            elif self.ImageIndex < 250:
                self.im2.drawSub(self.x, self.y, 58, 82, 686, 224, 58, 65)
            elif self.ImageIndex <= 300:
                self.im2.drawSub(self.x - 6, self.y, 67, 82, 619, 224, 67, 65)

            self.ImageIndex += 1

            if self.ImageIndex == 300:
                self.ImageIndex = 0
            self.a = 1


        elif ccircle.isKeyDown('d'):
            self.vx = 30
            if self.ImageIndex < 50:
                self.im.drawSub(self.x, self.y, 64, 82, 0, 224, 64, 65)

            elif self.ImageIndex < 100:
                self.im.drawSub(self.x+12, self.y, 49, 82, 66, 224, 47, 65)

            elif self.ImageIndex < 150:
                self.im.drawSub(self.x+4, self.y, 52, 82, 113, 224, 52, 65)

            elif self.ImageIndex < 200:
                self.im.drawSub(self.x-5, self.y, 66, 82, 167, 224, 64, 65)

            elif self.ImageIndex < 250:
                self.im.drawSub(self.x, self.y, 58, 82, 231, 224, 58, 65)
            elif self.ImageIndex <= 300:
                self.im.drawSub(self.x, self.y, 67, 82, 289, 224, 67, 65)

            self.ImageIndex += 1

            if self.ImageIndex == 300:
                self.ImageIndex = 0

            self.a = 2
        elif self.y > 382:
            if self.ImageIndex < 20:
                if self.a == 2:
                    self.im2.drawSub(self.x, self.y, 70, 86, 710, 323, 53, 80)
                if self.a == 1:
                    self.im.drawSub(self.x, self.y, 70, 86, 212, 323, 53, 80)
        elif self.y < 380:
            if self.a == 2:
                self.im.drawSub(self.x, self.y, 70, 82, 106, 312, 53, 80)
            else:
                self.im2.drawSub(self.x, self.y, 70, 86, 816, 323, 53, 80)
        else:
            if self.a == 1:
                self.im2.drawSub(self.x, self.y, 60, 82, 925, 27, 50, 70)
            else:
                self.im.drawSub(self.x, self.y, 60, 82, 0, 27, 50, 70)
            self.ImageIndex = 0




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
            self.jump = 0





        else:
            self.vx = 0

        if self.y < -150:
            self.y = -150
            self.vy = 0





