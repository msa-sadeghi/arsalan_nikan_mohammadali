from constants import *
from castle import Castle

castle = Castle(SCREEN_WIDTH- 280, SCREEN_HEIGHT-350)
bullet_group = pygame.sprite.Group()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False          
    screen.blit(bg, (0,0))
    castle.draw(screen)
    castle.shoot(bullet_group)
    bullet_group.draw(screen)
    bullet_group.update()
    pygame.display.update()
    clock.tick(FPS)