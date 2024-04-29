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
        group.add(self)      
    def update(self):
        self.rect.x += self.speed