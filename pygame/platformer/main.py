import pygame
from world import World

from player import Player
from button import Button
import pickle
level = 1

f = open("level1", "rb")
world_data = pickle.load(f)
f.close()


def next_level():
    global level
    level += 1
    f = open(f"level{level}", "rb")
    world_data = pickle.load(f)
    enemy_group.empty()
    door_group.empty()
    game_world = World(world_data, enemy_group, door_group)
    f.close()
    return game_world
    

pygame.init()
screen_width = 1024
screen_height = 704
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

restart_img = pygame.image.load("assets/restart_btn.png")
restart_button = Button(restart_img, screen_width/2, screen_height/2)


my_player = Player()
enemy_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
game_world = World(world_data, enemy_group, door_group)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    game_world.draw(screen)
    enemy_group.draw(screen)
    enemy_group.update()
    door_group.draw(screen)
    my_player.draw(screen)
    my_player.move(game_world.tile_map, enemy_group, door_group)
    if not my_player.alive:
        restart_button.draw(screen)
        if restart_button.click():
            my_player.__init__()
            enemy_group.empty()
            door_group.empty()
            game_world = World(world_data, enemy_group, door_group)
            
    if my_player.next_level:
        game_world = next_level()
        my_player.__init__()
    pygame.display.update()
    clock.tick(60)