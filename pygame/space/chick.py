from pygame.sprite import Sprite
from constants import *
from egg import Egg
import random
class Chick(Sprite):
    def __init__(self,x,y, chick_group, egg_group):
        super().__init__()
        self.image = pygame.image.load("assets/chick.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = 1
        self.speed = 4
        self.egg_group = egg_group
        chick_group.add(self)
        
    def update(self):
        self.rect.x += self.speed * self.direction
        self.fire()
        
    def fire(self):
        if random.randint(1,2000) > 1999:
            Egg(self.rect.centerx, self.rect.bottom, self.egg_group)
        