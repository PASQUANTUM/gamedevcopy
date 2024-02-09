import pygame
import json

"""
Parses a set of Images by given JSON data into seperate Images for Animation
Takes in filename as Argument
PNG and JSON need to be named the same to work
Called by all Animated Objects
"""

class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename)
        self.meta_data = self.filename.replace('png', 'json')

        #Loads the JSON Data of the File for parsing
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()



    def get_sprite(self, x, y, w, h):
        """
        Cuts out the Sprite from Spritesheet when given the Coordinates and Dimensions
        :param x: X coordinate
        :param y: Y Coordinate
        :param w: Width
        :param h: Height
        :return: Sprite Image of Spritesheet
        """
        sprite = pygame.Surface((w, h))
        """"
        Any Pixels with this Key will not be shown
        This Seperates the Image from The Background
        You should not use full Black if you want it displayed
        """
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet,(0, 0),(x, y, w, h))
        return sprite

    def parse_sprite(self, name):
        """
        Loads Coordinates and Dimensions from Metadata per filename the calls get_sprite

        Returns
        :param name:
        :return: image
        """
        sprite = self.data['frames'][name]['frame']
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.get_sprite(x, y, w, h)
        return image
