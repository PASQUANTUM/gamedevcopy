import pygame
from os import path

"""""
All States inherit from BaseState
sets Base Properties all States will need
"""""
class BaseState(object):
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pygame.display.get_surface().get_rect()
        self.persist = {}
        self.font = pygame.font.Font("assets/Pixel.ttf", 24)
        self.HS_FILE = "highscore.txt"

    def startup(self, persistent):
        """
        :param persistent:
        :return:
        """
        self.persist = persistent

    def get_event(self, event):
        """
        Event Handling
        :param event:
        :return:
        """
        pass

    def load_data(self):

        """
        Reads the Highscore

        :return:highscore
        """
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, self.HS_FILE), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        return self.highscore

    def update(self, dt):
        """
        Every state calls this to update
        :param dt:
        :return:
        """
        pass

    def draw(self, surface):
        """
        Every state calls this to draw
        :param surface:
        :return:
        """
        pass