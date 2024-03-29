import pygame
"""
This Obstical Removes 1 Point 
It gives a small additional Impuls
"""
class REDCIRCLE(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.width = 48
        self.height = 48
        self.image = pygame.image.load(f'assets/redcircle/redplanet2.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(center=pos)
        self.x = self.rect.x
        self.y = self.rect.y
        self.col_y = 5
        self.col_x = 5
        self.xspeed = 3

    def move(self):
        """
        Basic Movement from Wall to Wall
        :return:
        """

        self.rect.x += self.xspeed

        if self.rect.left < 640:
            self.impact()
        if self.rect.right > 640*2:
            self.impact()

    def impact(self):
        """
        On Impact changing Directions
        :return:
        """
        self.xspeed = self.xspeed * -1


    def update(self):
        """
        Updating Movement
        :return:
        """
        self.move()


