from constants import *
from castle import Castle
from enemy import Enemy
import random
import pygame
pygame.init()
level_difficulty = 0
MAX_DIFFICULTY = 1000
enemy_spawn_time = pygame.time.get_ticks()
enemy_group = pygame.sprite.Group()
j = 0
def spawn_enemies():
    global level_difficulty,j, enemy_spawn_time
    if level_difficulty < MAX_DIFFICULTY:
        if pygame.time.get_ticks() - enemy_spawn_time > 2000:
            enemy_spawn_time = pygame.time.get_ticks()
            i = random.randrange(ENEMY_NUMBERS)
            Enemy(ENEMY_TYPES[i], -100, 200 + j * 50, enemy_group, ENEMY_SPEEDS[i], ENEMY_HEALTHS[i], 0.3)
            level_difficulty += ENEMY_HEALTHS[i]
            j += 1

        

castle = Castle(SCREEN_WIDTH- 280, SCREEN_HEIGHT-350)
bullet_group = pygame.sprite.Group()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False          
    
    
    spawn_enemies()
    screen.blit(bg, (0,0))
    castle.draw(screen)
    castle.shoot(bullet_group)
    bullet_group.draw(screen)
    bullet_group.update()
    enemy_group.update(castle, bullet_group, screen)
    enemy_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)