import pygame
import os

WIDTH, HEIGHT = 800, 500
DARK_BLUE = (0, 0, 30)
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chicken Invaders")

# player spaceship
SPACESHIP = pygame.image.load(os.path.join("media", "spaceship.png"))
LASER = pygame.image.load(os.path.join("media", "laser.png"))
# enemy
CHICKEN = pygame.image.load(os.path.join("media", "chicken.png"))
# enemy attack
EGG = pygame.image.load(os.path.join("media", "egg.png"))

# background
BACKGROUND = pygame.image.load(os.path.join("media", "galaxy.jpg"))
