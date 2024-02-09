import sys
import pygame
from states.menu import Menu
from states.gameplay import Gameplay
from states.game_over import GameOver
from states.splash import Splash
from game import Game

""""
Main:

Makes Screen
Declares States that Class Game is running
Initiates Object of Game
Runs Game

"""

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
states = {
    "MENU": Menu(),
    "SPLASH": Splash(),
    "GAMEPLAY": Gameplay(),
    "GAME_OVER": GameOver(),
}

game = Game(screen, states, "SPLASH")
game.run()

pygame.quit()
sys.exit()