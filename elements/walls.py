import pygame

class WALL(pygame.sprite.Sprite):
    def __init__(self, pos,orientation):
        super().__init__()
        self.width = 10
        self.height = 1080
        self.image = pygame.image.load(f'assets/bumper/bumper1.png')
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(topright=pos)
        self.angle = 0
        if orientation == 2:
            self.image = pygame.transform.rotate(self.image, 30)
            self.rect = self.image.get_rect(center=(640,0))
            self.angle = 30
        if orientation == 3:
            self.image = pygame.transform.rotate(self.image, -30)
            self.rect = self.image.get_rect(center=(2*640,0))
            self.angle = -30
        self.x = self.rect.x
        self.y = self.rect.y