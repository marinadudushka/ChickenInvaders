import pygame
import spaceObject
import constants


class GoodPlayer(spaceObject.SpaceObject):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.object_img = constants.SPACESHIP
        self.weapon_img = constants.LASER
        self.mask = pygame.mask.from_surface(self.object_img)
        self.max_health = health
        self.lives = 5

    def move_fire(self, vel, objs):
        self.cool_down()
        for w in self.weapons:
            w.move(vel)
            if w.off_screen(constants.HEIGHT):
                self.weapons.remove(w)
            else:
                for obj in objs:
                    if w.collision(obj):
                        objs.remove(obj)
                        if w in self.weapons:
                            self.weapons.remove(w)

    def get_injured(self):
        self.health -= 10

    def die(self):
        self.lives -= 1

    def get_lives(self):
        return self.lives

    def get_health(self):
        return self.health

    def get_max_health(self):
        return self.max_health

    def restart_health(self):
        self.health = self.max_health


