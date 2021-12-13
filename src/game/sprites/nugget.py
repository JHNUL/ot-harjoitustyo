import os
import pygame

from constants import CELL_SIZE
dirname = os.path.dirname(__file__)


class Nugget(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "..", "assets", "proto_nugget.png")
        )
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
