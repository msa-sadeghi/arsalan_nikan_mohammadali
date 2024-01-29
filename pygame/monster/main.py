import random

from constants import *
from player import Player
from monster import Monster


monster_group = pygame.sprite.Group()
my_player = Player(player_image)
level = 0

def start_new_level():
    global level
    level += 1
    for i in range(level):
        monster1 = Monster(all_monster_images[0], random.randint(0, SCREEN_WIDTH), random.randint(100, SCREEN_HEIGHT - 100))
        monster_group.add(monster1)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    my_player.draw()
    pygame.display.update()
    clock.tick(FPS)
