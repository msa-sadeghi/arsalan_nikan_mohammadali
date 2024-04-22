from pygame.sprite import Sprite
import pygame
import math
class Bullet(Sprite):
    def __init__(self, x,y, direction, group):
        super().__init__()
        self.image =pygame.transform.scale(pygame.image.load("assets/bullet.png"), (32,32))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.direction = direction
        self.speed = 10
        group.add(self)
        
        
    def update(self):
        self.rect.x += math.cos(self.direction) * self.speed
        self.rect.y += -math.sin(self.direction) * self.speed
        