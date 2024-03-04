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
    def draw(self, screen):
        screen.blit(self.image, self.rect)