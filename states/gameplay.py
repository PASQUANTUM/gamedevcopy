import random

import pygame
from .base import BaseState
from spritesheet import Spritesheet
from elements.ball import BALL
from elements.canon import CANON
from elements.redcircle import REDCIRCLE
from elements.bumper import BUMPER
from elements.walls import WALL
from elements.logo import LOGO
from elements.point10circle import POINT10CIRCLE
from elements.rectangle import RECTANGLE
import random
from os import path

"""
Third State
State where the Game is actually played
Exits into GameOver

Game Objects are initiated at the start

Game ends if a Ball(Alien) falls to the Screen Bottom or on ESC
Numerous Balls can be spawned that vanish at GameOver


"""
class Gameplay(BaseState):
    def __init__(self):
        super(Gameplay, self).__init__()
        pygame.mixer.init()
        self.points_sound = pygame.mixer.Sound("assets/sounds/points.wav")
        self.points_sound.set_volume(0.5)
        self.next_state = "GAME_OVER"
        self.backgroundpicture = pygame.image.load('assets/background/backgroundpicture.png').convert_alpha()
        self.ballgroup1 = pygame.sprite.Group()
        self.canon = CANON((475+1920/3,0))
        self.redcircle = REDCIRCLE((1000,200))
        self.point10circlegroup = pygame.sprite.Group()
        self.point10circlegroup.add(POINT10CIRCLE((random.randint(675,1150), random.randint(400,800))))
        self.bumper1 = BUMPER((110+1920/3,950),1)
        self.bumper2 = BUMPER((400+1920/3, 950),2)
        self.wall1 = WALL((640, 0),1)
        self.wall2 = WALL((1280 , 0),1)
        self.rectangle3 = RECTANGLE((random.randint(800,850),random.randint(300,400)),random.randint(50,100))
        self.rectangle4 = RECTANGLE((random.randint(900,1200),random.randint(300,400)),random.randint(50,100))
        self.logo = LOGO((640,100))
        self.highscore = self.load_data()
        self.points = 0
        self.scoretext = f"SCORE: {self.points}"
        self.scoresurf = self.font.render(self.scoretext, True, "red")
        self.newhighscoretext = "NEW HIGHSCORE!"
        self.newhighscoresurf = self.font.render(self.newhighscoretext, True, "red")


    def ballcollide(self):
        """
        Loops through all balls in the game and checks for Collisions
        If a ball is Colliding Ball.Impact Function is called

        At collision with 10PointCircle,it will vanish and a new one randomly spawns
        10 Points are added

        At collision with Redcircle(red Planet) 1 Point is abducted
        :return:
        """
        for ball1 in self.ballgroup1:
            if ball1.is_distance_colliding(self.redcircle) == True:
                if self.points > 0:
                    self.points -= 1
                ball1.impact(self.redcircle)

            for point10circle in self.point10circlegroup:
                if ball1.is_distance_colliding(point10circle) == True:
                    self.points += 10
                    self.points_sound.play()
                    point10circle.kill()
                    self.point10circlegroup.add(POINT10CIRCLE((random.randint(675, 1150), random.randint(400, 800))))
            if ball1.is_aabb_colliding(self.bumper1) == True:
                ball1.impact(self.bumper1)
            if ball1.is_aabb_colliding(self.bumper2) == True:
                ball1.impact(self.bumper2)
            if ball1.is_aabb_colliding(self.wall1) == True:
                ball1.impact(self.wall1)
            if ball1.is_aabb_colliding(self.wall2) == True:
                ball1.impact(self.wall2)
            if ball1.is_aabb_colliding(self.rectangle3) == True:
                ball1.impact(self.rectangle3)
            if ball1.is_aabb_colliding(self.rectangle4) == True:
                ball1.impact(self.rectangle4)
    def writehighscorefunc(self):
        """
        Writes Highscore into Highscore.txt
        :return:
        """
        if self.points > self.highscore:
            self.highscore = self.points
            with open(path.join(self.dir, self.HS_FILE), 'w') as f:
                f.write(str(self.highscore))

    def get_event(self, event):
        """
        KEY Inputs
        Q and W to flip the Bumpers
        SPACE to spawn a BALL out of Canon
        :param event:
        :return:
        """
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.done = True
            if event.key == pygame.K_SPACE:
                self.ballgroup1.add(self.canon.createball1())
            if event.key == pygame.K_q:
                self.bumper1.flip = True
            if event.key == pygame.K_w:
                self.bumper2.flip = True

    def draw(self, surface):
        """
        Draws Background and all Game objects
        Draws Score
        Draws Highscore Message if hit
        :param surface:
        :return:
        """
        surface.blit(self.backgroundpicture, (-50, -900))
        surface.blit(self.canon.image, (self.canon.rect))
        surface.blit(self.redcircle.image, (self.redcircle.rect))
        surface.blit(self.bumper1.image, (self.bumper1.rect))
        surface.blit(self.bumper2.image, (self.bumper2.rect))
        surface.blit(self.wall1.image, (self.wall1.rect))
        surface.blit(self.wall2.image, (self.wall2.rect))
        surface.blit(self.rectangle3.image, (self.rectangle3.rect))
        surface.blit(self.rectangle4.image, (self.rectangle4.rect))
        #pygame.draw.polygon(surface, 'purple', self.bumper1.rectRotated())
        #pygame.draw.polygon(surface, 'blue', self.bumper2.rectRotated())
        #pygame.draw.polygon(surface, 'green', (self.bumper1.rect.topleft,self.bumper1.rect.topright,self.bumper1.rect.bottomright,self.bumper1.rect.bottomleft))
        #pygame.draw.polygon(surface, 'red', (self.bumper2.rect.topleft,self.bumper2.rect.topright,self.bumper2.rect.bottomright,self.bumper2.rect.bottomleft))
        surface.blit(self.logo.image, (self.logo.rect))
        self.ballgroup1.draw(surface)
        self.point10circlegroup.draw(surface)
        if self.points > self.highscore:
            surface.blit(self.newhighscoresurf, (1920 / 5 - 100, 50))
        surface.blit(self.scoresurf, (900, 50))

    def update(self, dt):
        """
        Updates all Game Objects

        :param dt:
        :return:
        """
        for ball1 in self.ballgroup1:
            if ball1.rect.bottom > 1080:
                for b in self.ballgroup1:
                    b.kill()
                self.writehighscorefunc()
                self.points = 0
                self.done = True
        self.redcircle.update()
        self.rectangle3.update()
        self.rectangle4.update()
        self.ballgroup1.update()
        self.ballcollide()
        self.bumper1.update()
        print(self.bumper2.rectRotated())
        self.bumper2.update()
        self.canon.update()
        self.logo.update()
        self.point10circlegroup.update()
        self.scoretext = f"SCORE: {self.points}"
        self.scoresurf = self.font.render(self.scoretext, True, "black")