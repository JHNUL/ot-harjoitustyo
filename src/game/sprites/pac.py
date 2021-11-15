import pygame
import os
dirname = os.path.dirname(__file__)


class Pac(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "..", "assets", "proto_pac.png")
        )

        self.rect = self.image.get_rect()

        self.rect.x = 100
        self.rect.y = 100
