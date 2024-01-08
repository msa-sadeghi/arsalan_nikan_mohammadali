import random
import pygame
pygame.init()


SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 700
FPS = 60


score = 0


clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
myfont = pygame.font.Font("font.otf",48)

title = myfont.render("Wolf game", True, (255,0,0))
title_rect = title.get_rect(top = 0, centerx = SCREEN_WIDTH/2)

pygame.mixer.music.load("Bad Piggies Theme.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

eat_sound = pygame.mixer.Sound("chomp.wav")


wolf_image = pygame.image.load("wolf.png")
wolf_rect = wolf_image.get_rect()
wolf_rect.bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT)

# لود کردن عکس ببعی
sheep_image = pygame.image.load("sheep.png")

sheep_image = pygame.transform.flip(sheep_image, True, False)

sheep_rect = sheep_image.get_rect()
sheep_rect.topleft = (0, random.randint(100, SCREEN_HEIGHT-100))

# main loop
running = True
while running:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and wolf_rect.top > 100:
        wolf_rect.y -= 5
    if keys[pygame.K_DOWN] and wolf_rect.bottom < SCREEN_HEIGHT:
        wolf_rect.y += 5
    if keys[pygame.K_LEFT] and wolf_rect.left > 0:
        wolf_rect.x -= 5
    if keys[pygame.K_RIGHT] and wolf_rect.right < SCREEN_WIDTH:
        wolf_rect.x += 5

    sheep_rect.x += 5

    if wolf_rect.colliderect(sheep_rect):
        score += 1
        sheep_rect.topleft = (0, random.randint(100, SCREEN_HEIGHT-100))
        eat_sound.play()


    if sheep_rect.right > SCREEN_WIDTH:
        sheep_rect.topleft = (0, random.randint(100, SCREEN_HEIGHT-100))



    screen.fill((0,0,0))
    screen.blit(title, title_rect)
    screen.blit(wolf_image, wolf_rect)
    screen.blit(sheep_image, sheep_rect)
    pygame.display.update()
    clock.tick(FPS)