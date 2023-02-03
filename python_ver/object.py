import pygame
from window import wind_width, wind_height

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, img_path):
		# setup
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        pass

    def move(self, x, y):
        self.rect = self.rect.move((x, y))

    def bound(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > wind_width():
            self.rect.right = wind_width()
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > wind_height():
            self.rect.bottom = wind_height()
