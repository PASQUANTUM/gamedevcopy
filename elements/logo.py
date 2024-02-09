import pygame
from spritesheet import Spritesheet

"""
Logo Animation with no Impact on Gameplay
"""
class LOGO(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()

        """
        Loading Spritesheet and Appending Sprite Images to Animation Array that will be looped over
        """
        self.spritesheet = Spritesheet('assets/logo/happyflipperlogo.png')
        self.basicanimation = []
        self.index = 0
        self.counter = 0
        self.width = 700
        self.height = 300

        for num in range(0, 14):
            img = self.spritesheet.parse_sprite(f"New Piskel{num}.png").convert_alpha()
            img = pygame.transform.scale(img, (self.width, self.height))
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
        if self.index >= 14:
            self.index = 0
        self.image = self.basicanimation[self.index]

    def update(self):
        """
        Updating the Animation
        :return:
        """
        self.animate()