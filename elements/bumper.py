import random

import pygame
import math


"""
Flippers can move Upwards and pass additional Speed to Ball
Different Orientations for more interesting Game Play
"""
class BUMPER(pygame.sprite.Sprite):
    def __init__(self, pos,orientation):
        super().__init__()
        self.width = 180
        self.height = 50
        self.image = pygame.image.load(f'assets/bumper/bumper1.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(center=pos)
        self.x = self.rect.x
        self.y = self.rect.y
        self.vel_y = 10
        self.col_y = 0
        self.col_x = 0
        self.flip = False

        self.orientation = orientation
        if self.orientation == 1:
            self.angle = 355
            self.image = pygame.transform.rotate(self.image, self.angle)

        if self.orientation == 2:
            self.angle = 5
            self.image = pygame.transform.rotate(self.image, self.angle)


    def flip_bumper(self):
        """
        This makes the Bumper 'jump' by altering the y speed
        :return:
        """

        if self.flip:
            self.rect.y -= self.vel_y * 2
            self.vel_y -= .5
            if self.vel_y < -10:
                self.vel_y = 10
                self.flip = False


    def rectRotated(self):
        """
        Function to rotate a Rectangle

        Potentially for use of Seperating Axis (SAT-Collisions)
        Returns new Points of Rectangle after Rotation

        Not used right now

        rotates Rect.
        rect: pygame.Rect
        rotation: int (degrees)
        return: (vertices)
        """

        newp1x = self.rect.topleft[0]*math.cos(math.radians(self.angle))-self.rect.topleft[1]*math.sin(math.radians(self.angle))
        newp1y = self.rect.topleft[0]*math.sin(math.radians(self.angle))+self.rect.topleft[1]*math.cos(math.radians(self.angle))
        newp2x = self.rect.topright[0]*math.cos(math.radians(self.angle))-self.rect.topright[1]*math.sin(math.radians(self.angle))
        newp2y = self.rect.topright[0]*math.sin(math.radians(self.angle))+self.rect.topright[1]*math.cos(math.radians(self.angle))
        newp3x = self.rect.bottomright[0]*math.cos(math.radians(self.angle))-self.rect.bottomright[1]*math.sin(math.radians(self.angle))
        newp3y = self.rect.bottomright[0]*math.sin(math.radians(self.angle))+self.rect.bottomright[1]*math.cos(math.radians(self.angle))
        newp4x = self.rect.bottomleft[0]*math.cos(math.radians(self.angle))-self.rect.bottomleft[1]*math.sin(math.radians(self.angle))
        newp4y = self.rect.bottomleft[0]*math.sin(math.radians(self.angle))+self.rect.bottomleft[1]*math.cos(math.radians(self.angle))

        newp1 = newp1x, newp1y
        newp2 = newp2x, newp2y
        newp3 = newp3x, newp3y
        newp4 = newp4x, newp4y

        return newp1,newp2,newp3,newp4

    def update(self):
        """
        Depending on Orientation of Bumper it gives a Different Impuls to Ball
        :return:
        """
        self.flip_bumper()
        if self.flip:
            self.col_y = random.randint(17,20)
            if self.orientation == 2:
                self.col_x = random.randint(3,5)

            else:
                self.col_x = -1*random.randint(3, 5)

        else: self.col_y = 0