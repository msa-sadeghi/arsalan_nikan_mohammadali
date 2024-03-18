import pygame
from world import World
from level1 import world_data
from player import Player
pygame.init()
screen_width = 1024
screen_height = 704
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

my_player = Player()
enemy_group = pygame.sprite.Group()
game_world = World(world_data, enemy_group)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    game_world.draw(screen)
    enemy_group.draw(screen)
    enemy_group.update()
    my_player.draw(screen)
    my_player.move(game_world.tile_map, enemy_group)
    pygame.display.update()
    clock.tick(60)