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
import random
from os import path

class Gameplay(BaseState):
    def __init__(self):
        super(Gameplay, self).__init__()
        self.next_state = "GAME_OVER"
        self.ballgroup1 = pygame.sprite.Group()
        self.canon = CANON((475+1920/3,0))
        self.redcircle = REDCIRCLE((1000,200))
        self.point10circlegroup = pygame.sprite.Group()
        self.point10circlegroup.add(POINT10CIRCLE((random.randint(675,1150), random.randint(400,800))))
        self.bumper1 = BUMPER((100+1920/3,950),1)
        self.bumper2 = BUMPER((400+1920/3, 950),2)
        self.wall1 = WALL((640, 0),1)
        self.wall2 = WALL((1280 , 0),1)
        self.wall3 = WALL((640, 0),2)
        self.wall4 = WALL((1280 , 0),3)
        self.logo = LOGO((640,100))
        self.highscore = self.load_data()
        self.points = 0
        self.scoretext = f"SCORE: {self.points}"
        self.scoresurf = self.font.render(self.scoretext, True, "red")
        self.newhighscoretext = "NEW HIGHSCORE!"
        self.newhighscoresurf = self.font.render(self.newhighscoretext, True, "red")


    def ballcollide(self):
        for ball1 in self.ballgroup1:
            if ball1.is_distance_colliding(self.redcircle) == True:
                ball1.kill()

            for point10circle in self.point10circlegroup:
                if ball1.is_distance_colliding(point10circle) == True:
                    self.points += 10
                    point10circle.kill()
                    self.point10circlegroup.add(POINT10CIRCLE((random.randint(675, 1150), random.randint(400, 800))))
            if ball1.is_aabb_colliding(self.bumper1) == True:
                ball1.impact(self.bumper1.col_y)
            if ball1.is_aabb_colliding(self.bumper2) == True:
                ball1.impact(self.bumper2.col_y)
            if ball1.is_aabb_colliding(self.wall1) == True:
                ball1.impact()
            if ball1.is_aabb_colliding(self.wall2) == True:
                ball1.impact()
            if ball1.is_aabb_colliding(self.wall3) == True:
                ball1.impact()
            if ball1.is_aabb_colliding(self.wall4) == True:
                ball1.impact()
                
    def highscorefunc(self):
        if self.points > self.highscore:
            self.highscore = self.points
            with open(path.join(self.dir, self.HS_FILE), 'w') as f:
                f.write(str(self.highscore))

    def get_event(self, event):
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
        surface.fill(pygame.Color("grey"))
        surface.blit(self.canon.image, (self.canon.rect))
        surface.blit(self.redcircle.image, (self.redcircle.rect))
        surface.blit(self.bumper1.image, (self.bumper1.rect))
        surface.blit(self.bumper2.image, (self.bumper2.rect))
        surface.blit(self.wall1.image, (self.wall1.rect))
        surface.blit(self.wall2.image, (self.wall2.rect))
        surface.blit(self.wall3.image, (self.wall3.rect))
        surface.blit(self.wall4.image, (self.wall4.rect))
        surface.blit(self.logo.image, (self.logo.rect))
        self.ballgroup1.draw(surface)
        self.point10circlegroup.draw(surface)
        if self.points > self.highscore: surface.blit(self.newhighscoresurf, (1920 / 2 - 100, 1080 / 2))
        surface.blit(self.scoresurf, (0, 0))

    def update(self, dt):
        for ball1 in self.ballgroup1:
            if ball1.rect.bottom > 1080:
                for b in self.ballgroup1:
                    b.kill()
                    self.highscorefunc()
                    self.points = 0
                self.done = True
        self.redcircle.update()
        self.ballgroup1.update()
        self.ballcollide()
        self.bumper1.update()
        self.bumper2.update()
        self.canon.update()
        self.logo.update()
        self.point10circlegroup.update()
        self.scoretext = f"SCORE: {self.points}"
        self.scoresurf = self.font.render(self.scoretext, True, "black")