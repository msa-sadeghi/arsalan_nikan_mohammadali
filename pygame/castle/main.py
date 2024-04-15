from constants import *
from castle import Castle

castle = Castle(SCREEN_WIDTH- 280, SCREEN_HEIGHT-350)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False          
    screen.blit(bg, (0,0))
    castle.draw(screen)
    pygame.display.update()
    clock.tick(FPS)