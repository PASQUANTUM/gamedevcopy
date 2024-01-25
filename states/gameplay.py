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

class Gameplay(BaseState):
    def __init__(self):
        super(Gameplay, self).__init__()
        self.next_state = "GAME_OVER"
        self.ballgroup1 = pygame.sprite.Group()
        self.ballgroup2 = pygame.sprite.Group()
        self.canon = CANON((475+1920/3,0))
        self.redcircle = REDCIRCLE((1000,500))
        self.point10circlegroup = pygame.sprite.Group()
        self.point10circlegroup.add(POINT10CIRCLE((random.randint(675,1150), random.randint(400,800))))
        self.bumper1 = BUMPER((100+1920/3,950),1)
        self.bumper2 = BUMPER((400+1920/3, 950),2)
        self.wall1 = WALL((640, 0))
        self.wall2 = WALL((1280 , 0))
        self.logo = LOGO((640,100))

    def ballcollide(self):
        for ball1 in self.ballgroup1:
            if ball1.is_distance_colliding(self.redcircle) == True:
                ball1.kill()

            for point10circle in self.point10circlegroup:
                if ball1.is_distance_colliding(point10circle) == True:
                    point10circle.kill()
                    self.point10circlegroup.add(POINT10CIRCLE((random.randint(675, 1150), random.randint(400, 800))))
            if ball1.is_aabb_colliding(self.bumper1) == True:
                ball1.impact(self.bumper1.vel_y)
            if ball1.is_aabb_colliding(self.bumper2) == True:
                ball1.impact(self.bumper2.vel_y)
            if ball1.is_aabb_colliding(self.bumper2) == True:
                ball1.impact(self.bumper2.vel_y)
            if ball1.is_aabb_colliding(self.bumper2) == True:
                ball1.impact(self.bumper2.vel_y)
        for ball2 in self.ballgroup2:
            if ball2.is_distance_colliding(self.redcircle) == True:
                ball2.impact()

        for ball2 in self.ballgroup2:
            if ball2.is_aabb_colliding(self.bumper1) == True or ball2.is_aabb_colliding(self.bumper2) == True:
                ball2.impact()


    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.done = True
            if event.key == pygame.K_SPACE:
                self.ballgroup2.add(self.canon.createball2())
            if event.key == pygame.K_x:
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
        surface.blit(self.logo.image, (self.logo.rect))
        self.ballgroup1.draw(surface)
        self.ballgroup2.draw(surface)
        self.point10circlegroup.draw(surface)

    def update(self, dt):
        for ball1 in self.ballgroup1:
            if ball1.rect.bottom > 1080:
                for b in self.ballgroup1:
                    b.kill()
                #self.done = True
        self.redcircle.update()
        self.ballgroup2.update()
        self.ballgroup1.update()
        self.ballcollide()
        self.bumper1.update()
        self.bumper2.update()
        self.canon.update()
        self.logo.update()
        self.point10circlegroup.update()