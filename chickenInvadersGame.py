import pygame
import random
import constants
import weapon
from chicken import Chicken

pygame.font.init()


class Game:

    def __init__(self, pl):
        self.clock = pygame.time.Clock()
        # game
        self.main_font = pygame.font.SysFont("arial", 25)
        self.game_over_font = pygame.font.SysFont("arial", 50)
        self.run = True
        self.game_over = False
        self.game_over_count = 0
        # player stuff
        self.hero = pl
        self.level = 0
        self.wave_length = 5
        self.fire_vel = 4
        # enemy
        self.chickens_list = []
        self.chicken_vel = 1
        self.move_velocity = 5

    def redraw_window(self):
        constants.WIN.blit(constants.BACKGROUND, (0, 0))

        lives_count = self.main_font.render(f"Lives: {self.hero.get_lives()}", True, (255, 255, 255))
        level_count = self.main_font.render(f"Level: {self.level}", True, (255, 255, 255))

        pygame.draw.rect(constants.WIN, (255, 0, 0), (10, lives_count.get_height() + 10, lives_count.get_width(), 10))
        pygame.draw.rect(constants.WIN, (0, 255, 0), (10, lives_count.get_height() + 10, lives_count.get_width()*(self.hero.get_health()/self.hero.get_max_health()), 10))
        constants.WIN.blit(lives_count, (10, 10))
        constants.WIN.blit(level_count, (constants.WIDTH - level_count.get_width() - 10, 10))

        for c in self.chickens_list:
            c.draw(constants.WIN)

        self.hero.draw(constants.WIN)

        if self.game_over:
            game_over_text = self.game_over_font.render("Game Over!", True, (255, 255, 255))
            constants.WIN.blit(game_over_text, (constants.WIDTH / 2 - game_over_text.get_width() / 2, 200))
        pygame.display.update()

    def play(self):
        while self.run:
            self.clock.tick(constants.FPS)
            self.redraw_window()

            if self.hero.get_health() <= 0 and self.hero.get_lives() > 0 and not self.game_over:
                self.hero.die()
                self.hero.restart_health()

            if self.hero.get_lives() <= 0 or self.hero.get_health() <= 0:
                self.game_over = True
                self.game_over_count += 1

            if self.game_over:
                if self.game_over_count > constants.FPS * 3:
                    run = False
                    quit()
                else:
                    continue
            if len(self.chickens_list) == 0:
                self.level += 1
                self.wave_length += 5
                for i in range(self.wave_length):
                    c = Chicken(random.randrange(50, constants.WIDTH - 100), random.randrange(-1500, -100))
                    self.chickens_list.append(c)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                run = False
                quit()
                break
            if keys[pygame.K_LEFT] and self.hero.x - self.move_velocity > 0:
                self.hero.x -= self.move_velocity
            if keys[pygame.K_RIGHT] and self.hero.x + self.move_velocity + self.hero.get_width() < constants.WIDTH:
                self.hero.x += self.move_velocity
            if keys[pygame.K_UP] and self.hero.y - self.move_velocity > 0:
                self.hero.y -= self.move_velocity
            if keys[pygame.K_DOWN] and self.hero.y + self.move_velocity + self.hero.get_height() < constants.HEIGHT:
                self.hero.y += self.move_velocity
            if keys[pygame.K_SPACE]:
                self.hero.shoot()

            for chicken in self.chickens_list[:]:
                chicken.move(self.chicken_vel)
                chicken.move_fire(self.fire_vel, self.hero)
                if random.randrange(0, 2 * constants.FPS) == 1:
                    chicken.shoot()
                if weapon.collide(chicken, self.hero):
                    self.hero.get_injured()
                    self.chickens_list.remove(chicken)
                elif chicken.y + chicken.get_height() > constants.HEIGHT:
                    self.hero.die()
                    self.chickens_list.remove(chicken)

            self.hero.move_fire(-self.fire_vel, self.chickens_list)

    def game_menu(self):
        game_title_font = pygame.font.SysFont("arial", 70)

        self.run = True
        while self.run:
            constants.WIN.blit(constants.BACKGROUND, (0, 0))
            game_title = game_title_font.render("Click the mouse to start!", True, (255, 255, 255))
            constants.WIN.blit(game_title, (constants.WIDTH/2 - game_title.get_width()/2, 200))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.play()
        pygame.quit()
