import pygame
class Button:
    def __init__(self, image, x,y):
        self.image = image
        self.rect = self.image.get_rect(center=(x,y))
        self.last_clicked = False
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def click(self):
        clicked = False
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] and not self.last_clicked:
                clicked = True
                self.last_clicked = True
        if not pygame.mouse.get_pressed()[0]:
            self.last_clicked = False
                
        return clicked