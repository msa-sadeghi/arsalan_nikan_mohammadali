from constants import *
from player import Player
from chick import Chick
player_bullet_group = pygame.sprite.Group()
my_player = Player(player_bullet_group)
chick_group = pygame.sprite.Group()
egg_group = pygame.sprite.Group()

def spawn_chick():
    for i in range(4):
        for j in range(8):
            Chick(j * 96, i * 96, chick_group,egg_group)
            
spawn_chick()
level = 1          
def check_edge_collision():
    on_edge = False
    for chick in chick_group:
        if chick.rect.left < 0 or chick.rect.right > SCREEN_WIDTH:
            on_edge = True
            break
    if on_edge:
        for chick in chick_group:
            chick.rect.y += 10 * level
            chick.direction *= -1

def check_bullet_collisions():
    if pygame.sprite.groupcollide(player_bullet_group, chick_group, True, True):
        pass
    if pygame.sprite.spritecollide(my_player, egg_group, True):
        pass

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                my_player.fire()
    check_edge_collision() 
    check_bullet_collisions()           
    screen.fill((0,0,0)) 
    chick_group.update()
    chick_group.draw(screen)
    egg_group.update()
    egg_group.draw(screen)
    player_bullet_group.update()
    player_bullet_group.draw(screen)
    my_player.draw()
    my_player.move()
    pygame.display.update()
    clock.tick(FPS)