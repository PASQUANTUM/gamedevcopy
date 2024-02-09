import random
from spritesheet import Spritesheet
import pygame
"""
Cool KIT Obsticles for diverse Gamplay
"""
class RECTANGLE(pygame.sprite.Sprite):
    def __init__(self, pos,width):
        super().__init__()
        self.spritesheet = Spritesheet('assets/logo/PhysikRectangle.png')
        self.basicanimation = []
        self.index = 0
        self.counter = 0
        self.width = width
        self.height = width
        """
        Additional Collision Imuls on Ball (here 0)
        """
        self.col_y = 0
        self.col_x = 0

        for num in range(0, 6):
            img = self.spritesheet.parse_sprite(f"New Piskel{num}.png").convert_alpha()
            img = pygame.transform.scale(img, (self.width,self.width))
            self.basicanimation.append(img)

        self.image = self.basicanimation[self.index]
        self.rect = self.image.get_rect(topleft=pos)

    def animate(self):
        """
        Current Image is set by current Index of Basicanimation
        Index is Looping through the Length of the Array
        :return:
        """
        speed = 20
        self.counter += 1
        if self.counter >= speed and self.index < len(self.basicanimation):
            self.counter = 0
            self.index += 1
        if self.index >= 6:
            self.index = 0
        self.image = self.basicanimation[self.index]

    def update(self):
        """
        Updating the Animation
        :return:
        """
        self.animate()
