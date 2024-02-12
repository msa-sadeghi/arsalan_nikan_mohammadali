from pygame.sprite import Sprite
from constants import *
class Egg(Sprite):
    def __init__(self, x,y, egg_group):
        super().__init__()
        self.image = pygame.image.load("assets/egg.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        egg_group.add(self)
        
    
    def update(self):
        self.rect.y += 5
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.kill()
        