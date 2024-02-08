import pygame
import random
import math

from spritesheet import Spritesheet

BOUNCE_STOP = 4

class BALL(pygame.sprite.Sprite):

    def __init__(self, pos, img):
        super().__init__()

        if img == 1:
            self.width = 48
            self.height = 48
        else:
            self.width = 64
            self.height = 64

        self.image = pygame.image.load(f'assets//ball/ball{img}.png')
        self.rect = self.image.get_rect(center = pos)
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
            self.rect.centerx += self.xspeed * 0.3
            self.rect.centery += self.yspeed * 0.3
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
        self.rect.centerx += self.xspeed*0.55
        self.rect.centery += self.yspeed*0.55

    #Test

    def update(self):
        self.move()

