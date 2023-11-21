import pygame
from .base import BaseState
from spritesheet import Spritesheet

class Gameplay(BaseState):
    def __init__(self):
        super(Gameplay, self).__init__()
        self.next_state = "GAME_OVER"

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.done = True

    def draw(self, surface):
        surface.fill(pygame.Color("black"))