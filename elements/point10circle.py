import pygame

class POINT10CIRCLE(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.width = 64
        self.height = 64
        self.image = pygame.image.load(f'assets/point10circle.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(center=pos)
        self.x = self.rect.x
        self.y = self.rect.y

