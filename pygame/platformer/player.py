from pygame.sprite import Sprite
import pygame

class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.right_images = []
        self.left_images = []
        for i in range(1,5):
            img = pygame.image.load(f"assets/guy{i}.png")
            left_img = pygame.transform.flip(img, True, False)
            self.right_images.append(img)
            self.left_images.append(left_img)
        self.frame_index = 0
        self.image = self.right_images[self.frame_index]
        self.rect = self.image.get_rect(topleft=(100,500))
        self.alive = True
        self.score = 0
        self.health = 3
        self.direction = 1
        self.yvelocity = 0
        self.jumped = False
        self.jump_sound = pygame.mixer.Sound("assets/jump.wav")
        self.last_update_time = pygame.time.get_ticks()
        self.moving = False
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def animation(self):
        if pygame.time.get_ticks() - self.last_update_time > 200:
            self.last_update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.right_images):
            self.frame_index = 0
        if not self.moving:
            self.frame_index = 0
        if self.direction == 1:
            self.image = self.right_images[self.frame_index]
        elif self.direction == -1:
            self.image = self.left_images[self.frame_index]
            
        
    def move(self, tiles):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = -1
            self.moving = True
            dx -= 5
        if keys[pygame.K_RIGHT]:
            self.direction = 1
            self.moving = True
            dx += 5
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.moving = False
        if keys[pygame.K_SPACE] and not self.jumped:
            self.jump_sound.play()
            self.yvelocity = -15
            self.jumped = True
            
        dy += self.yvelocity
        self.yvelocity += 1
        for t in tiles:
            if t[1].colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                dx = 0
            if t[1].colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                if self.yvelocity > 0:
                    self.yvelocity = 0
                    dy = t[1].top - self.rect.bottom
                    self.jumped = False
                else:
                    self.yvelocity = 0
                    dy = t[1].bottom - self.rect.top
            
        self.rect.x += dx
        self.rect.y += dy
        self.animation()