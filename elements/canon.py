import pygame
from .ball import BALL
from spritesheet import Spritesheet
import time


"""
Canon is only used for Spawning the Ball
"""
class CANON(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        """
        Creating Instance of Spritesheet with Filename to get Parsed Sprites
        Adding Images into Different Arrays:
        basicanimation & shootanimation
        to alter the animation based on the canons Action
        """
        self.spritesheet = Spritesheet('assets/canon/canonbasic.png')
        self.basicanimation = []
        self.spritesheetshoot = Spritesheet('assets/canon/canonshoot.png')
        self.shootanimation = []
        self.index = 0
        self.counter = 0
        self.width = 128*1.25
        self.height = 128*1.35
        self.shooting = False
        self.vel_y = 10
        self.countanimation1 = 907
        self.countanimation2 = 10

        for num in range(0, 4):
            img = self.spritesheet.parse_sprite(f"New Piskel{num}.png").convert_alpha()
            img = pygame.transform.scale(img, (self.width, self.height))
            self.basicanimation.append(img)

        for num in range(0, 4):
            img = self.spritesheetshoot.parse_sprite(f"New Piskel{num}.png").convert_alpha()
            img = pygame.transform.scale(img, (self.width, self.height))
            self.shootanimation.append(img)

        self.image = self.basicanimation[self.index]
        self.rect = self.image.get_rect(topleft=(pos[0],1080-self.height))

    def animate(self):
        """
        THe basic Animation Indeces are Getting Looped until Canon is Shooting
        While Shooting The Shooting Animation is played
        :return:
        """
        if self.shooting == False:
            speed = 20
            self.counter += 1
            if self.counter >= speed and self.index < len(self.basicanimation):
                self.counter = 0
                self.index -= 1
            if self.index < 0:
                self.index = 3
            self.image = self.basicanimation[self.index]
        elif self.shooting == True:
            speed = 5
            self.counter += 1
            if self.counter >= speed and self.index < len(self.shootanimation):
                self.counter = 0
                self.index -= 1
            if self.index < 0:
                self.index = 3
            self.image = self.shootanimation[self.index]


    def animationcount(self):
        """
        Counts for The Time the Animation is Lasting
        :return:
        """
        if self.shooting == True:
            self.countanimation1 -= self.countanimation2 * 2
            self.countanimation2 -= .5
            if self.countanimation2 < -1:
                self.shooting = False
                self.countanimation2 = 10



    def createball1(self):
        """
        Creates BAll at own Coordinates
        :return: Object of Class BAll
        """
        self.shooting = True
        return BALL((self.rect.x+80, self.rect.top-30),52,52)

    def update(self):
        """
        Updating The Animations
        :return:
        """
        self.animationcount()
        self.animate()

