import random
import pygame
pygame.init()
screen = pygame.display.set_mode()
SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()
FPS = 60
clock = pygame.time.Clock()
wolf_image = pygame.image.load("assets/wolf.png")
wolf_rect = wolf_image.get_rect(centerx = SCREEN_WIDTH/2, bottom = SCREEN_HEIGHT)
meat_image = pygame.image.load("assets/meat.png")
meat_rect = meat_image.get_rect(left = random.randint(0, SCREEN_WIDTH- meat_image.get_width()), top = 100)
font = pygame.font.Font("assets/font.otf", 28)

score = 0
wolf_normal_speed = 5
wolf_boost_speed = 20
wolf_speed = wolf_normal_speed
STARTING_BOOST_LEVEL = 100
boost_level = STARTING_BOOST_LEVEL

boost_text = font.render(f"Boost: {boost_level}", True, (10,230,210))
boost_rect = boost_text.get_rect(centerx = SCREEN_WIDTH/2 , top = 0)

score_text = font.render(f"score: {score}", True, (10,230,210))
score_rect = score_text.get_rect(topleft=(0,0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and wolf_rect.left >=0:
        wolf_rect.x -= wolf_speed
    if keys[pygame.K_RIGHT] and wolf_rect.right <= SCREEN_WIDTH:
        wolf_rect.x += wolf_speed
    if keys[pygame.K_SPACE] and boost_level >0:
        boost_level -= 1
        wolf_speed = wolf_boost_speed
    if not keys[pygame.K_SPACE] or boost_level <= 0:
        wolf_speed = wolf_normal_speed
    
    if wolf_rect.colliderect(meat_rect):
        score += 1
        meat_rect = meat_image.get_rect(left =random.randint(0, SCREEN_WIDTH- meat_image.get_width()), top = 100)
        
    
    meat_rect.y += 5
    if meat_rect.top >= SCREEN_HEIGHT:
        meat_rect = meat_image.get_rect(left =random.randint(0, SCREEN_WIDTH- meat_image.get_width()), top = 100)
    boost_text = font.render(f"Boost: {boost_level}", True, (10,230,210))
    score_text = font.render(f"score: {score}", True, (10,230,210))
    screen.fill((0,0,0))
    screen.blit(boost_text, boost_rect)
    screen.blit(wolf_image, wolf_rect)
    screen.blit(meat_image, meat_rect)
    screen.blit(score_text, score_rect)
    pygame.display.update()
    clock.tick(FPS)