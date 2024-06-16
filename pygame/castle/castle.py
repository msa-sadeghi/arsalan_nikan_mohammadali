from pygame.sprite import Sprite
from constants import *
from bullet import Bullet
import math
class Castle(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image_100 = pygame.transform.scale(castle_100, (castle_100.get_width() * 0.2, castle_100.get_height() * 0.2))
        self.image_50 = pygame.transform.scale(castle_50, (castle_50.get_width() * 0.2, castle_50.get_height() * 0.2))
        self.image_25 = pygame.transform.scale(castle_25, (castle_25.get_width() * 0.2, castle_25.get_height() * 0.2))
        self.image = self.image_100
        self.rect = self.image.get_rect(topleft = (x,y))
        self.is_clicked = False
        self.health = 1000
        self.max_health = 1000
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def shoot(self, group):
        if pygame.mouse.get_pressed()[0] and not self.is_clicked:
            self.is_clicked = True
            mouse_pos = pygame.mouse.get_pos()
            yd = -(mouse_pos[1] - self.rect.midleft[1])
            xd = mouse_pos[0] - self.rect.midleft[0]
            Bullet(self.rect.midleft[0], self.rect.midleft[1], math.atan2(yd,xd), group)
        if not pygame.mouse.get_pressed()[0]:
            self.is_clicked = False
        