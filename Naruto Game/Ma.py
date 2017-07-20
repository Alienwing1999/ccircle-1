import ccircle



class Char:
    def __init__(self, image, image2, world):
        self.type = 'character'
        self.x = 400
        self.y = 360
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
        self.a = 2
        self.ImageIndex = 0
        self.jump = 0
        self.pl = 0
        self.health = 100
        self.lives = 3
        self.world = world

        #self.rspeed = 0

    def apply_force(self, fx, fy):
        self.fx += fx
        self.fy += fy

    def draw(self, window):

        if ccircle.isKeyDown('u'):
            if self.a == 2:
                if self.ImageIndex < 25:
                    self.im.drawSub(self.x, self.y, 57, 80, 10, 539, 50, 69)

                elif self.ImageIndex < 50:
                    self.im.drawSub(self.x, self.y, 59, 80, 60, 539, 52, 69)

                elif self.ImageIndex < 75:
                    self.im.drawSub(self.x, self.y, 67, 80, 112, 539, 58, 69)

                elif self.ImageIndex < 100:
                    self.im.drawSub(self.x, self.y, 73, 80, 170, 539, 64, 69)

                elif self.ImageIndex <= 125:
                    self.im.drawSub(self.x, self.y, 76, 80, 234, 539, 66, 69)

                elif self.ImageIndex <= 150:
                    self.im.drawSub(self.x, self.y, 69, 80, 300, 539, 60, 69)

                self.ImageIndex += 1
                if self.ImageIndex == 150:
                    self.ImageIndex = 0
            if self.a == 1:
                if self.ImageIndex < 25:
                    self.im2.drawSub(self.x, self.y, 57, 80, 915, 539, 50, 69)

                elif self.ImageIndex < 50:
                    self.im2.drawSub(self.x, self.y, 59, 80, 863, 539, 52, 69)

                elif self.ImageIndex < 75:
                    self.im2.drawSub(self.x, self.y, 67, 80, 805, 539, 58, 69)

                elif self.ImageIndex < 100:
                    self.im2.drawSub(self.x, self.y, 73, 80, 741, 539, 64, 69)

                elif self.ImageIndex <= 125:
                    self.im2.drawSub(self.x, self.y, 76, 80, 675, 539, 66, 69)

                elif self.ImageIndex <= 150:
                    self.im2.drawSub(self.x, self.y, 69, 80, 615, 539, 60, 69)

                self.ImageIndex += 1
                if self.ImageIndex == 150:
                    self.ImageIndex = 0
        elif ccircle.isKeyDown('i'):
            damage = 10
            for players in self.world.objects:
                if players.x > self.x + 50 / 2 and players.x < self.x + 100:
                    if self.y > self.y and self.y < self.y + 120:
                        players.health -= damage

            if self.a == 2:
                if self.ImageIndex < 25:
                    self.im.drawSub(self.x, self.y, 60, 80, 13, 1344, 56, 74)
                    self.im.drawSub(self.x + 80, self.y - 12, 108, 125, 70, 1340, 100, 115)

                elif self.ImageIndex < 50:
                    self.im.drawSub(self.x, self.y, 60, 80, 13, 1344, 56, 74)
                    self.im.drawSub(self.x + 80, self.y - 12, 142, 125, 200, 1340, 130, 115)

                elif self.ImageIndex < 75:
                    self.im.drawSub(self.x, self.y, 60, 80, 13, 1344, 56, 74)
                    self.im.drawSub(self.x + 80, self.y - 16, 142, 125, 371, 1340, 130, 115)

                elif self.ImageIndex < 100:
                    self.im.drawSub(self.x, self.y, 60, 80, 13, 1344, 56, 74)
                    self.im.drawSub(self.x + 80, self.y - 17, 142, 125, 564, 1340, 130, 115)

                elif self.ImageIndex <= 125:
                    self.im.drawSub(self.x, self.y, 60, 80, 13, 1344, 56, 74)
                    self.im.drawSub(self.x + 80, self.y - 29, 142, 125, 750, 1340, 130, 115)

                elif self.ImageIndex <= 150:
                    self.im.drawSub(self.x, self.y, 60, 80, 13, 1344, 56, 74)
                    self.im.drawSub(self.x + 80, self.y - 33, 142, 125, 20, 1440, 130, 115)

                elif self.ImageIndex <= 175:
                    self.im.drawSub(self.x, self.y, 60, 80, 13, 1344, 56, 74)
                    self.im.drawSub(self.x + 80, self.y - 37, 142, 125, 218, 1440, 130, 115)

                elif self.ImageIndex < 200:
                    self.im.drawSub(self.x, self.y, 60, 80, 13, 1344, 56, 74)
                    self.im.drawSub(self.x + 80, self.y - 39, 142, 125, 371, 1440, 130, 115)

                elif self.ImageIndex < 225:
                    self.im.drawSub(self.x, self.y, 60, 80, 13, 1344, 56, 74)
                    self.im.drawSub(self.x + 80, self.y-41, 142, 125, 564, 1440, 130, 115)

                elif self.ImageIndex <= 250:
                    self.im.drawSub(self.x, self.y, 60, 80, 13, 1344, 56, 74)
                    self.im.drawSub(self.x + 80, self.y-43, 142, 125, 750, 1440, 130, 115)

                self.ImageIndex += 1

                if self.ImageIndex == 250:
                    self.ImageIndex = 0

            if self.a == 1:

                if self.ImageIndex < 15:
                    self.im2.drawSub(self.x, self.y, 75, 95, 972, 860, 67, 85)

                elif self.ImageIndex < 30:
                    self.im2.drawSub(self.x, self.y, 75, 95, 905, 860, 67, 85)

                elif self.ImageIndex < 45:
                    self.im2.drawSub(self.x, self.y, 75, 95, 838, 860, 67, 85)

                elif self.ImageIndex < 60:
                    self.im2.drawSub(self.x, self.y, 75, 95, 771, 860, 67, 85)

                elif self.ImageIndex <= 75:
                    self.im2.drawSub(self.x, self.y, 75, 95, 704, 860, 67, 85)

                elif self.ImageIndex <= 90:
                    self.im2.drawSub(self.x, self.y, 75, 95, 637, 860, 67, 85)

                elif self.ImageIndex <= 105:
                    self.im2.drawSub(self.x, self.y, 75, 95, 570, 860, 67, 85)

                elif self.ImageIndex < 120:
                    self.im2.drawSub(self.x, self.y, 75, 95, 447, 860, 67, 85)

                elif self.ImageIndex < 135:
                    self.im2.drawSub(self.x, self.y, 75, 95, 365, 860, 67, 85)

                elif self.ImageIndex <= 150:
                    self.im2.drawSub(self.x, self.y, 75, 95, 283, 860, 67, 85)

                self.ImageIndex += 1

                if self.ImageIndex == 405:
                    self.ImageIndex = 0



        elif ccircle.isKeyDown('w'):
            if self.a == 2:
                if self.ImageIndex < 5:
                    self.im.drawSub(self.x-6, self.y-2, 70, 82, 0, 323, 53, 80)

                elif self.ImageIndex < 10:
                    self.im.drawSub(self.x, self.y, 70, 82, 53, 323, 53, 80)

                else:
                    self.im.drawSub(self.x, self.y, 70, 82, 106, 312, 53, 80)

                self.ImageIndex += 1

                if ccircle.isKeyDown('a'):
                    self.vx = -35
                    self.a = 1
                if ccircle.isKeyDown('d'):
                    self.vx = 35
                    self.a = 2

            else:
                if self.ImageIndex < 5:
                    print('a')
                    self.im2.drawSub(self.x+6, self.y+2, 70, 82, 922, 323, 53, 80)

                elif self.ImageIndex < 10:
                    print('b')
                    self.im2.drawSub(self.x, self.y, 70, 82, 869, 323, 53, 80)

                else:
                    print('c')
                    self.im2.drawSub(self.x, self.y, 70, 82, 816, 312, 53, 80)
                if ccircle.isKeyDown('a'):
                    self.vx = -35
                    self.a = 1
                if ccircle.isKeyDown('d'):
                    self.vx = 35
                    self.a = 2
                self.ImageIndex += 1
            if self.jump == 0:
                self.vy = -125
                self.jump += 1

        elif ccircle.isKeyDown('a'):
            self.vx = -35
            if self.jump == 0:
                if self.ImageIndex < 50:
                    self.im2.drawSub(self.x, self.y, 64, 82, 911, 224, 64, 65)

                elif self.ImageIndex < 100:
                    self.im2.drawSub(self.x, self.y, 49, 82, 860, 224, 47, 65)

                elif self.ImageIndex < 150:
                    self.im2.drawSub(self.x + 5, self.y, 52, 82, 810, 224, 52, 65)

                elif self.ImageIndex < 200:
                    self.im2.drawSub(self.x, self.y, 66, 82, 742, 224, 64, 65)

                elif self.ImageIndex < 250:
                    self.im2.drawSub(self.x, self.y, 58, 82, 686, 224, 58, 65)

                elif self.ImageIndex <= 300:
                    self.im2.drawSub(self.x - 6, self.y, 67, 82, 619, 224, 67, 65)
            else:
                self.im2.drawSub(self.x, self.y, 70, 82, 816, 312, 53, 80)
            self.ImageIndex += 1

            if self.ImageIndex == 300:
                self.ImageIndex = 0
            self.a = 1


        elif ccircle.isKeyDown('d'):
            self.vx = 35
            if self.jump == 0:
                if self.ImageIndex < 50:
                    self.im.drawSub(self.x, self.y, 64, 82, 0, 224, 64, 65)

                elif self.ImageIndex < 100:
                    self.im.drawSub(self.x + 12, self.y, 49, 82, 66, 224, 47, 65)

                elif self.ImageIndex < 150:
                    self.im.drawSub(self.x + 4, self.y, 52, 82, 113, 224, 52, 65)

                elif self.ImageIndex < 200:
                    self.im.drawSub(self.x - 5, self.y, 66, 82, 167, 224, 64, 65)

                elif self.ImageIndex < 250:
                    self.im.drawSub(self.x, self.y, 58, 82, 231, 224, 58, 65)
                elif self.ImageIndex <= 300:
                    self.im.drawSub(self.x, self.y, 67, 82, 289, 224, 67, 65)
            else:
                self.im.drawSub(self.x, self.y, 70, 82, 106, 312, 53, 80)
            self.ImageIndex += 1

            if self.ImageIndex == 300:
                self.ImageIndex = 0

            self.a = 2


        elif self.a == 2 and self.pl == 1:
            self.im.drawSub(self.x, self.y, 60, 82, 0, 27, 50, 70)
            self.ImageIndex = 0
        elif self.a == 1 and self.pl == 1:
            self.im2.drawSub(self.x, self.y, 60, 82, 925, 27, 50, 70)
            self.ImageIndex = 0

        elif self.y < 370:
            if self.a == 2:
                self.im.drawSub(self.x, self.y, 70, 82, 106, 312, 53, 80)
            elif self.a == 1:
                self.im2.drawSub(self.x, self.y, 70, 86, 816, 323, 53, 80)
            self.ImageIndex = 0
        else:
            if self.a == 1:
                self.im2.drawSub(self.x, self.y, 60, 82, 925, 27, 50, 70)
            if self.a == 2:
                self.im.drawSub(self.x, self.y, 60, 82, 0, 27, 50, 70)
            self.ImageIndex = 0
            self.vx = 0




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

        if self.y > 370 and self.y < 385:
            if self.x > 130 and self.x < 960:
                self.y = 371
                self.vy = 0
                self.jump = 0

        else:
            self.vx = 0


        if self.y > 215 and self.y < 235:
            if self.vy >= 0:
                if self.x > 223 and self.x < 420:
                    self.vy = 0
                    self.y = 216
                    self.jump = 0
                    self.pl = 1

        else:
            self.vx = 0


        if self.y > 215 and self.y < 235:
            if self.vy >= 0:
                if self.x > 665 and self.x < 874:
                    self.vy = 0
                    self.jump = 0
                    self.y = 216
                    self.pl = 1

        else:
            self.vx = 0

        if self.y > 80 and self.y < 100:
            if self.vy >= 0:
                if self.x > 446 and self.x < 648:
                    self.vy = 0
                    self.jump = 0
                    self.y = 81
                    self.pl = 1



        else:
            self.vx = 0

        if self.y < -150:
            self.y = -150
            self.vy = 0


