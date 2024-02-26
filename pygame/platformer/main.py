import pygame
from world import World
from level1 import world_data
pygame.init()
screen_width = 1024
screen_height = 704
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game_world = World(world_data)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    game_world.draw(screen)
    pygame.display.update()
    clock.tick(60)