import pygame

class BUMPER(pygame.sprite.Sprite):
    def __init__(self, pos, orientation):
        super().__init__()
        self.width = 128
        self.height = 42
        self.image = pygame.image.load(f'assets/bumper1.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(center=pos)
        self.x = self.rect.x
        self.y = self.rect.y
        self.vel_y = 10
        self.flip = False


    def flip_bumper(self):
        if self.flip:
            self.rect.y -= self.vel_y * 2
            self.vel_y -= .5
            if self.vel_y < -10:
                self.flip = False
                self.vel_y = 10


    def update(self):
        self.flip_bumper()