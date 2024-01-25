import pygame

class WALL(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.width = 10
        self.height = 20000
        self.image = pygame.image.load(f'assets/bumper1.png')
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(center=pos)
        self.x = self.rect.x
        self.y = self.rect.y