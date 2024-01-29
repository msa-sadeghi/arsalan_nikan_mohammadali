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
        monster1 = Monster(all_monster_images[0], random.randint(0, SCREEN_WIDTH), random.randint(100, SCREEN_HEIGHT - 100),0)
        monster_group.add(monster1)
        monster2 = Monster(all_monster_images[1], random.randint(0, SCREEN_WIDTH), random.randint(100, SCREEN_HEIGHT - 100),1)
        monster_group.add(monster2)
        monster3 = Monster(all_monster_images[2], random.randint(0, SCREEN_WIDTH), random.randint(100, SCREEN_HEIGHT - 100),2)
        monster_group.add(monster3)
        monster4 = Monster(all_monster_images[3], random.randint(0, SCREEN_WIDTH), random.randint(100, SCREEN_HEIGHT - 100),3)
        monster_group.add(monster4)
start_new_level()

def draw():
    global target_monster_image, target_monster_image_rect
    target_monster_image_rect = target_monster_image.get_rect(bottom = 100, centerx = SCREEN_WIDTH/2)
    # TODO display score, playerLives, levelNumber
    pygame.draw.rect(screen, (190,10,180), (0,100, SCREEN_WIDTH, SCREEN_HEIGHT-200), 5)
    screen.blit(target_monster_image, target_monster_image_rect)
    

def select_target_monster():
    global target_monster_image, target_monster_type
    target = random.choice(monster_group.sprites())
    target_monster_image = target.image
    target_monster_type = target.type
    

select_target_monster()


def check_collisions():
    collided_monster = pygame.sprite.spritecollideany(my_player, monster_group)
    if collided_monster:
        if collided_monster.type == target_monster_type:
            collided_monster.remove(monster_group)
            if len(monster_group) != 0:
                select_target_monster()
            else:
                start_new_level()



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.fill((0,0,0))
    check_collisions()
    draw()
    my_player.move()
    my_player.draw()
    monster_group.update()
    monster_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
