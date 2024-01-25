import pygame
import random
import math

from spritesheet import Spritesheet

BOUNCE_STOP = 4

class BALL(pygame.sprite.Sprite):

    def __init__(self, pos, img):
        super().__init__()
        if img == 1:
            self.width = 32
            self.height = 32
        else:
            self.width = 64
            self.height = 64

        self.image = pygame.image.load(f'assets/ball{img}.png')
        self.rect = self.image.get_rect(center = pos)
        self.gravity = .5
        self.xspeed = random.randint(-10,-1)
        self.yspeed = -20
        self.retention = 0.75

    def move(self):
        self.rect.y += self.yspeed
        self.rect.x += self.xspeed

        if self.rect.top < 0:
            self.impact()
        if self.rect.left < 640:
            self.impact()
        if self.rect.right > 640*2:
            self.impact()
        if self.rect.bottom < 1081:
            self.yspeed += self.gravity
        else:
             if self.yspeed > BOUNCE_STOP:
                 self.yspeed = self.yspeed * -1 * self.retention
             if abs(self.yspeed) <= BOUNCE_STOP:
                self.yspeed = 0

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

    def is_overlapping_collision(self, other):
        if self.rect.x == other.rect.x and self.rect.y == other.rect.y:
            return True
        else:
            return False

    def impact(self,other_y_vel = 0):
        if other_y_vel == 0:
            other_y_vel = 0
        else:
            other_y_vel = other_y_vel
            print('vel',other_y_vel)
            self.yspeed = other_y_vel
        self.xspeed = self.xspeed * -1 * self.retention

    #Test

    def update(self):
        self.move()

