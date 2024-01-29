import pygame
pygame.init()
screen = pygame.display.set_mode()
SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()
clock = pygame.time.Clock()
FPS = 60
player_image = pygame.image.load("assets/player.png")
all_monster_images = []
for i in range(1,7):
    all_monster_images.append(pygame.image.load(f"assets/monster{i}.png"))

