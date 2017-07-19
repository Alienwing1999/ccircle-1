import ccircle



class Char:
    def __init__(self, image, image2):
        self.type = 'character'
        self.x = 500
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
        self.a = 1
        self.ImageIndex = 0
        self.jump = 0
        self.pl = 0
        self.health = 100

        #self.rspeed = 0

    def apply_force(self, fx, fy):
        self.fx += fx
        self.fy += fy

    def draw(self, window):

        if ccircle.isKeyDown('u'):
            if self.a == 2:
                if self.ImageIndex < 25:
                    self.im.drawSub(self.x, self.y-15, 56, 95, 647, 558, 65, 96)

                elif self.ImageIndex < 50:
                    self.im.drawSub(self.x, self.y-15, 61, 95, 712, 558, 70, 96)

                elif self.ImageIndex < 75:
                    self.im.drawSub(self.x, self.y-15, 112, 95, 782, 558, 131, 96)

                elif self.ImageIndex < 100:
                    self.im.drawSub(self.x, self.y-15, 60, 95, 913, 558, 69, 96)

                elif self.ImageIndex <= 125:
                    self.im.drawSub(self.x, self.y-15, 52, 95, 982, 558, 60, 96)
                self.ImageIndex += 1
                if self.ImageIndex == 125:
                    self.ImageIndex = 0
            if self.a == 1:
                if self.ImageIndex < 25:
                    self.im2.drawSub(self.x, self.y-15, 56, 95, 342, 558, 65, 96)

                elif self.ImageIndex < 50:
                    self.im2.drawSub(self.x, self.y-15, 61, 95, 272, 558, 70, 96)

                elif self.ImageIndex < 75:
                    self.im2.drawSub(self.x - 50, self.y-15, 112, 95, 141, 558, 131, 96)

                elif self.ImageIndex < 100:
                    self.im2.drawSub(self.x, self.y-15, 60, 95, 72, 558, 69, 96)

                elif self.ImageIndex <= 125:
                    self.im2.drawSub(self.x, self.y-15, 52, 95, 12, 558, 60, 96)
                self.ImageIndex += 1
                if self.ImageIndex == 125:
                    self.ImageIndex = 0
        elif ccircle.isKeyDown('i'):
            if self.a == 2:
                if self.ImageIndex < 15:
                    self.im.drawSub(self.x, self.y, 75, 95, 15, 860, 67, 85)

                elif self.ImageIndex < 30:
                    self.im.drawSub(self.x, self.y, 75, 95, 82, 860, 67, 85)

                elif self.ImageIndex < 45:
                    self.im.drawSub(self.x, self.y, 75, 95, 149, 860, 67, 85)

                elif self.ImageIndex < 60:
                    self.im.drawSub(self.x, self.y, 75, 95, 216, 860, 67, 85)

                elif self.ImageIndex <= 75:
                    self.im.drawSub(self.x, self.y, 75, 95, 283, 860, 67, 85)

                elif self.ImageIndex <= 90:
                    self.im.drawSub(self.x, self.y, 75, 95, 350, 860, 67, 85)

                elif self.ImageIndex <= 105:
                    self.im.drawSub(self.x, self.y, 75, 95, 417, 860, 67, 85)

                elif self.ImageIndex < 120:
                    self.im.drawSub(self.x, self.y, 75, 95, 540, 860, 67, 85)

                elif self.ImageIndex < 135:
                    self.im.drawSub(self.x, self.y, 75, 95, 622, 860, 67, 85)

                elif self.ImageIndex <= 150:
                    self.im.drawSub(self.x, self.y, 75, 95, 704, 860, 67, 85)

                elif self.ImageIndex <= 165:
                    self.im.drawSub(self.x, self.y, 75, 95, 786, 860, 67, 85)

                elif self.ImageIndex <= 180:
                    self.im.drawSub(self.x, self.y, 75, 95, 868, 860, 67, 85)

                elif self.ImageIndex < 195:
                    self.im.drawSub(self.x - 59, self.y, 193, 120, 15, 965, 193, 120)

                elif self.ImageIndex <= 210:
                    self.im.drawSub(self.x - 59, self.y, 193, 120, 208, 965, 193, 120)

                elif self.ImageIndex <= 225:
                    self.im.drawSub(self.x - 59, self.y, 193, 120, 401, 965, 193, 120)

                elif self.ImageIndex <= 240:
                    self.im.drawSub(self.x - 59, self.y, 193, 120, 594, 965, 193, 120)
                self.ImageIndex += 1
                if self.ImageIndex == 240:
                    self.ImageIndex = 0
            '''
            if self.a == 1:
                if self.ImageIndex < 25:
                    self.im2.drawSub(self.x, self.y-15, 56, 95, 342, 558, 65, 96)

                elif self.ImageIndex < 50:
                    self.im2.drawSub(self.x, self.y-15, 61, 95, 272, 558, 70, 96)

                elif self.ImageIndex < 75:
                    self.im2.drawSub(self.x - 50, self.y-15, 112, 95, 141, 558, 131, 96)

                elif self.ImageIndex < 100:
                    self.im2.drawSub(self.x, self.y-15, 60, 95, 72, 558, 69, 96)

                elif self.ImageIndex <= 125:
                    self.im2.drawSub(self.x, self.y-15, 52, 95, 12, 558, 60, 96)
                self.ImageIndex += 1
                if self.ImageIndex == 125:
                    self.ImageIndex = 0
            '''
        elif ccircle.isKeyDown('w'):
            if self.a == 2:
                if self.ImageIndex < 5:
                    self.im.drawSub(self.x, self.y, 70, 82, 15, 440, 68, 80)

                elif self.ImageIndex < 10:
                    self.im.drawSub(self.x, self.y, 70, 82, 83, 440, 68, 80)

                else:
                    self.im.drawSub(self.x, self.y, 70, 82, 160, 446, 80, 75)

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
                    self.im2.drawSub(self.x, self.y, 70, 82, 971, 440, 68, 80)

                elif self.ImageIndex < 10:
                    print('b')
                    self.im2.drawSub(self.x, self.y, 70, 82, 903, 440, 68, 80)

                else:
                    print('c')
                    self.im2.drawSub(self.x, self.y, 70, 82, 814, 446, 80, 75)
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
                    self.im2.drawSub(self.x, self.y, 89, 82, 598, 325, 76, 70)

                elif self.ImageIndex < 100:
                    self.im2.drawSub(self.x, self.y, 93, 82, 518, 325, 80, 70)

                elif self.ImageIndex < 150:
                    self.im2.drawSub(self.x, self.y, 91, 82, 441, 325, 77, 70)

                elif self.ImageIndex < 200:
                    self.im2.drawSub(self.x, self.y, 95, 82, 360, 325, 81, 70)

                elif self.ImageIndex < 250:
                    self.im2.drawSub(self.x, self.y, 100, 82, 274, 325, 86, 70)
            else:
                self.im2.drawSub(self.x, self.y, 70, 82, 814, 446, 80, 75)
            self.ImageIndex += 1

            if self.ImageIndex == 250:
                self.ImageIndex = 0
            self.a = 1


        elif ccircle.isKeyDown('d'):
            self.vx = 35
            if self.jump == 0:
                if self.ImageIndex < 50:
                    self.im.drawSub(self.x, self.y, 89, 82, 380, 325, 76, 70)

                elif self.ImageIndex < 100:
                    self.im.drawSub(self.x, self.y, 93, 82, 456, 325, 80, 70)

                elif self.ImageIndex < 150:
                    self.im.drawSub(self.x, self.y, 91, 82, 536, 325, 77, 70)

                elif self.ImageIndex < 200:
                    self.im.drawSub(self.x, self.y, 95, 82, 613, 325, 81, 70)

                elif self.ImageIndex < 250:
                    self.im.drawSub(self.x, self.y, 100, 82, 694, 325, 86, 70)
            else:
                self.im.drawSub(self.x, self.y, 70, 82, 160, 446, 80, 75)
            self.ImageIndex += 1

            if self.ImageIndex == 250:
                self.ImageIndex = 0

            self.a = 2


        elif self.a == 2 and self.pl == 1:
            self.im.drawSub(self.x, self.y, 66, 82, 16, 190, 65, 81)
            self.ImageIndex = 0
        elif self.a == 1 and self.pl == 1:
            self.im2.drawSub(self.x, self.y, 66, 82, 973, 190, 65, 81)
            self.ImageIndex = 0

        elif self.y < 370:
            if self.a == 2:
                self.im.drawSub(self.x, self.y, 70, 82, 160, 446, 80, 75)
            elif self.a == 1:
                self.im2.drawSub(self.x, self.y, 70, 82, 814, 446, 80, 75)
            self.ImageIndex = 0
        else:
            if self.a == 1:
                self.im2.drawSub(self.x, self.y, 66, 82, 973, 190, 65, 81)
            if self.a == 2:
                self.im.drawSub(self.x, self.y, 66, 82, 16, 190, 65, 81)
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



        if self.y > 215 and self.y < 235:
            if self.vy >= 0:
                if self.x > 223 and self.x < 420:
                    self.vy = 0
                    self.y = 216
                    self.jump = 0
                    self.pl = 1


        if self.y > 215 and self.y < 235:
            if self.vy >= 0:
                if self.x > 665 and self.x < 874:
                    self.vy = 0
                    self.jump = 0
                    self.y = 216
                    self.pl = 1

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





