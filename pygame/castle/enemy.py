from pygame.sprite import Sprite
import pygame
class Enemy(Sprite):
    def __init__(self, type, x,y, group, speed, health, scale):
        super().__init__()
        self.all_images = {}
        animation_types = ("walk", "attack", "death")
        for animation in animation_types:
            temp = []
            for i in range(20):
                img = pygame.image.load(f"assets/enemies/{type}/{animation}/{i}.png")
                w = img.get_width()
                h = img.get_height()
                img = pygame.transform.scale(img, (w * scale, h * scale))
                temp.append(img)
            self.all_images[animation] = temp
        self.image_number = 0
        self.action = "walk"
        self.image =  self.all_images[self.action][self.image_number]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.speed = speed
        self.health = health
        self.max_health = health
        self.alive = True
        group.add(self)  
        self.last_update_time = pygame.time.get_ticks()  
        self.last_attack_time = pygame.time.get_ticks()  
        self.font = pygame.font.SysFont("arial", 18)
    def update(self, castle, bullet_group, screen):
      
            
        
        if self.alive:
            if self.health >= self.max_health/2:
                color = (0,0,0)
            else:
                color = (255,0,0)
            t = self.font.render(str(self.health), True, color)
            r = t.get_rect()
            r.bottom = self.rect.top
            r.centerx = self.rect.centerx
            screen.blit(t, r)
            
            if pygame.sprite.spritecollide(self, bullet_group, True):
                self.health -= 25
                if self.health <= 0:
                    self.health = 0
                    self.update_action("death")
                    self.alive = False
                    castle.money += 100
            if self.rect.right > castle.rect.left:
                self.update_action("attack")
            if self.action == "walk":
                self.rect.x += self.speed
            if self.action == "attack":
                if pygame.time.get_ticks() - self.last_attack_time > 1000:
                    self.last_attack_time = pygame.time.get_ticks()
                    castle.health -= 25
                    if castle.health < 0:
                        castle.health = 0
            
        self.animation()
        
    def animation(self):
        self.image =  self.all_images[self.action][self.image_number]
        if pygame.time.get_ticks() - self.last_update_time > 100:
            self.last_update_time = pygame.time.get_ticks()
            self.image_number += 1
        if self.image_number >= len(self.all_images[self.action]):
            if self.action == "death":
                self.image_number = len(self.all_images[self.action]) - 1
            else:
                self.image_number = 0
    def update_action(self,new_action):
        if self.action != new_action:
            self.action = new_action
            self.image_number = 0