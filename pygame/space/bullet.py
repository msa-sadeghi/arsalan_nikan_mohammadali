from pygame.sprite import Sprite
import pygame
class Bullet(Sprite):
    def __init__(self, x,y, bullet_group):
        super().__init__()
        self.image = pygame.image.load("assets/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        bullet_group.add(self)
        
    
    def update(self):
        self.rect.y -= 5
        if self.rect.top <= 0:
            self.kill()
        