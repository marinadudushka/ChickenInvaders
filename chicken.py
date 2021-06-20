import pygame
import spaceObject
import constants
from weapon import Weapon


class Chicken(spaceObject.SpaceObject):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.object_img = constants.CHICKEN
        self.weapon_img = constants.EGG
        self.mask = pygame.mask.from_surface(self.object_img)

    def move(self, vel):
        self.y += vel


