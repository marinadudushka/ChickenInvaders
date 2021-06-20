import pygame
import constants
import weapon
import constants


class SpaceObject:

    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.object_img = None
        self.weapon_img = None
        self.weapons = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.object_img, (self.x, self.y))
        for w in self.weapons:
            w.draw(window)

    def move_fire(self, vel, obj):
        self.cool_down()
        for w in self.weapons:
            w.move(vel)
            if w.off_screen(constants.HEIGHT):
                self.weapons.remove(w)
            elif w.collision(obj):
                obj.health -= 10
                self.weapons.remove(w)

    def shoot(self):
        if self.cool_down_counter == 0:
            fire = weapon.Weapon(self.x, self.y, self.weapon_img)
            self.weapons.append(fire)
            self.cool_down_counter = 1

    def cool_down(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def get_width(self):
        return self.object_img.get_width()

    def get_height(self):
        return self.object_img.get_height()


