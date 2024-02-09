import pygame
import random
import math

from spritesheet import Spritesheet

BOUNCE_STOP = 4

class BALL(pygame.sprite.Sprite):

    def __init__(self, pos,width,height):
        super().__init__()
        self.width = width
        self.height = height
        self.spritesheet = Spritesheet('assets/ball/alien.png')
        self.basicanimation = []
        self.index = 0
        self.counter = 0


        for num in range(0, 5):
            img = self.spritesheet.parse_sprite(f"New Piskel{num}.png").convert_alpha()
            img = pygame.transform.scale(img, (self.width,self.width))
            self.basicanimation.append(img)


        #self.image = self.basicanimation[self.index]
        self.image = pygame.image.load('assets/ball/alien2.png')
        self.image = pygame.transform.scale(img, (self.width,self.width))
        self.rect = self.image.get_rect(topleft=pos)

        self.gravity = .5
        self.xspeed = -1 * random.randint(3,5)
        self.yspeed = -20
        self.retention = 0.75

    def move(self):
        self.rect.y += self.yspeed
        self.rect.x += self.xspeed

        if self.rect.top < 0:
            self.xspeed = self.xspeed * -1 * self.retention
            self.yspeed = self.yspeed * -1 * self.retention
            self.rect.centerx += self.xspeed * 0.5
            self.rect.centery += self.yspeed * 0.5
        if self.rect.bottom < 1081:
            self.yspeed += self.gravity
        else:
            print(self.yspeed)
            print(self.xspeed)
            if self.yspeed > BOUNCE_STOP:
                self.yspeed = self.yspeed * -1 * self.retention
                self.xspeed = self.xspeed * -1 * self.retention
            if abs(self.yspeed) <= BOUNCE_STOP:
                self.yspeed = 0
                self.xspeed = 0


    def animate(self):
        self.counter += 1
        if self.counter >= speed and self.index < len(self.basicanimation):
            self.counter = 0
            self.index += 1
        if self.index >= 5:
            self.index = 0
        self.image = self.basicanimation[self.index]

    def is_distance_colliding(self, other):
        distance = (((self.rect.centerx-other.rect.centerx) ** 2) + ((self.rect.centery-other.rect.centery) ** 2)) ** 0.5
        if distance < (self.width + other.width)/2.0:
            return True
        else:
            return False

    def is_aabb_colliding(self, other):
        # Axis Aligned Bounding Box
        x_collision = (math.fabs(self.rect.centerx - other.rect.centerx) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.rect.centery - other.rect.centery) * 2) < (self.height + other.height)
        return (x_collision and y_collision)
    
    def checkxorycol(self, other):
    #
        x_collision = (math.fabs(self.rect.centerx - other.rect.centerx) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.rect.centery - other.rect.centery) * 2) < (self.height + other.height)
        return x_collision ,y_collision

    def is_overlapping_collision(self, other):
        if self.rect.x == other.rect.x and self.rect.y == other.rect.y:
            return True
        else:
            return False

    def impact(self,other):

        print(other,other.rect.topleft,other.rect.topright,other.rect.bottomleft,other.rect.bottomright)
        self.xspeed = self.xspeed * -1 * self.retention - other.col_x
        self.yspeed = self.yspeed * -1 * self.retention - other.col_y
        self.rect.centerx += self.xspeed*0.5
        self.rect.centery += self.yspeed*0.5

    #Test

    def update(self):
        self.move()
        #self.animate()

