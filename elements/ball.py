import pygame
import random
import math

from spritesheet import Spritesheet

"""
Main Element of The Game
Gets spawned by canon

Affected by Gravity
Gets YSpeed and random XSpeed when spawned (Shooting out of the canon)
Is affected by Retention
"""


#To prevent the BAll bouncing infinite Times
BOUNCE_STOP = 4

class BALL(pygame.sprite.Sprite):

    def __init__(self, pos,width,height):
        super().__init__()
        pygame.mixer.init()
        self.collide_sound = pygame.mixer.Sound("assets/sounds/collide.wav")
        self.width = width
        self.height = height
        self.image = pygame.image.load('assets/ball/alien2.png')
        self.image = pygame.transform.scale(self.image, (self.width,self.width))
        self.rect = self.image.get_rect(topleft=pos)
        self.gravity = .5
        self.xspeed = -1*random.randint(1,5)
        self.yspeed = -20
        self.retention = 0.75

    def move(self):
        """
        The X-Y Coordinates are changed by current Speed
        Applying Gravity
        Preventing infinite Bounces
        :return:
        """
        self.rect.y += self.yspeed
        self.rect.x += self.xspeed

        if self.rect.top < 0:
            #Not Done in Impact Function because Top of Screen is not a Object with Rect
            self.xspeed = self.xspeed * -1 * self.retention
            self.yspeed = self.yspeed * -1 * self.retention
            self.rect.centerx += self.xspeed * 0.5
            self.rect.centery += self.yspeed * 0.5
            self.collide_sound.play()
        if self.rect.bottom < 1081:
            self.yspeed += self.gravity
        else:
            print(self.yspeed)
            print(self.xspeed)
            if self.yspeed > BOUNCE_STOP:
                self.yspeed = self.yspeed * -1 * self.retention
                self.xspeed = self.xspeed * -1 * self.retention
            if abs(self.yspeed) <= BOUNCE_STOP:
                self.yspeed = 0
                self.xspeed = 0

    def is_distance_colliding(self, other):
        """
        Collsion for Ball-Ball
        Distance between objects centers is checked by Pythagoras
        If Distance is Less than both radians/2 the Objects are colliding
        :param other: Object we are colliding  with
        :return:True or False
        """
        distance = (((self.rect.centerx-other.rect.centerx) ** 2) + ((self.rect.centery-other.rect.centery) ** 2)) ** 0.5
        if distance < (self.width + other.width)/2.0:
            return True
        else:
            return False

    def is_aabb_colliding(self, other):
        """

        Axis-Aligned Bounding Box Collision
        Collision for Rectangle-Rectangle or Ball-BAll
        Checks if Distane The XY-Coordinates of the Centers is Less than both Widths or Heights
        -> If both are True they are Colliding
        Math.fabs returns the absolute Value as a Float
        :param other: Object we are colliding  with
        :return: True or False
        """
        x_collision = (math.fabs(self.rect.centerx - other.rect.centerx) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.rect.centery - other.rect.centery) * 2) < (self.height + other.height)
        return (x_collision and y_collision)
    
    def checkxorycol(self, other):
        """
        :param other: Object we are colliding  with
        :return: X_Collsion(Bool) and Y_Collision(Bool)
        """
        x_collision = (math.fabs(self.rect.centerx - other.rect.centerx) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.rect.centery - other.rect.centery) * 2) < (self.height + other.height)
        return x_collision ,y_collision

    def impact(self,other):
        """
        The X and Y Speed are inverted
        An additional X and Y Speed Can be given by colliding Objects represanting an Impuls
        :param other: Object we are colliding  with
        :return:
        """


        """
        For Testing Purposes and bettering the Collisions the Corners of Colliding our Object were given
        print(other,other.rect.topleft,other.rect.topright,other.rect.bottomleft,other.rect.bottomright)
        """

        self.xspeed = self.xspeed * -1 * self.retention - other.col_x
        self.yspeed = self.yspeed * -1 * self.retention - other.col_y
        """
        This is Important to not keep The Ball in the Colliding Object
        The Tick the  Impact is Applied the Object might still be in The Colliding Object
        Therefore we move it out by a portion of its Speed
        """
        self.rect.centerx += self.xspeed*0.5
        self.rect.centery += self.yspeed*0.5
        self.collide_sound.play()

    #Test

    def update(self):
        """
        Updating the Movement
        :return:
        """
        self.move()

