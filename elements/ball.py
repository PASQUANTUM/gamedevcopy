import pygame

from spritesheet import Spritesheet

class BALL(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.width = 100
        self.height = 50