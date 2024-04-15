from pygame.sprite import Sprite
from constants import *

class Castle(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image_100 = pygame.transform.scale(castle_100, (castle_100.get_width() * 0.2, castle_100.get_height() * 0.2))
        self.image_50 = pygame.transform.scale(castle_50, (castle_50.get_width() * 0.2, castle_50.get_height() * 0.2))
        self.image_25 = pygame.transform.scale(castle_25, (castle_25.get_width() * 0.2, castle_25.get_height() * 0.2))
        self.image = self.image_100
        self.rect = self.image.get_rect(topleft = (x,y))
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)