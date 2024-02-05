import pygame

class BUMPER(pygame.sprite.Sprite):
    def __init__(self, pos, orientation):
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
        self.flip = False

    def flip_bumper(self):
        if self.flip:
            self.rect.y -= self.vel_y * 2
            self.vel_y -= .5
            if self.vel_y < -10:
                self.vel_y = 10
                self.flip = False


    def update(self):
        self.flip_bumper()
        if self.flip: self.col_y = 20
        else: self.col_y = 0