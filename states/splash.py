import pygame
from .base import BaseState
from spritesheet import Spritesheet

"""
First State
Plays Splash Logo & Sound without interaction
Exits into Menu after certain Time

Super Constructor runs BaseClass Constructor
"""

class Splash(BaseState):
    def __init__(self):
        super(Splash, self).__init__()
        pygame.mixer.init()
        self.splashsound = pygame.mixer.Sound("assets/sounds/splash.mp3")
        self.myspritesheet0 = Spritesheet("assets/logo/splashlogo.png")
        self.startlogoanimations = []
        for num in range (0,31):
            img = self.myspritesheet0.parse_sprite(f"New Piskel{num}.png")
            img = pygame.transform.scale(img,(1920,1080))
            self.startlogoanimations.append(img)
        self.index = 0
        self.counter = 0
        self.next_state = "MENU"
        self.time_active = 0
        self.splashsound.play()

    def update(self, dt):
        """
        Counts to 2.2 seconds then self.done = True
        :param dt:
        :return:
        """
        speed = 4
        self.counter += 1
        if self.counter >= speed and self.index < len(self.startlogoanimations)-1:
            self.counter = 0
            self.index += 1
        self.time_active += dt
        if self.time_active >= 2200:#2200
            self.index = 0
        if self.time_active >= 2200:
            self.done = True

    def draw(self, surface):
        """

        :param surface:
        :return:
        """
        surface.fill(pygame.Color("black"))
        surface.blit(self.startlogoanimations[self.index],(400,1080/2-350))
