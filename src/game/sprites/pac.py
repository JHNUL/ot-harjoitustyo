import os
import pygame

from constants import CELL_SIZE
dirname = os.path.dirname(__file__)


class Pac(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.lives = 3
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "..", "assets", "proto_pac.png")
        )
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.ephemeral = False
        self.timer = 1000

    def move(self, direction, walls):
        d_x, d_y = 0, 0
        if direction == pygame.K_LEFT:
            d_x, d_y = -CELL_SIZE, 0
        elif direction == pygame.K_RIGHT:
            d_x, d_y = CELL_SIZE, 0
        elif direction == pygame.K_UP:
            d_x, d_y = 0, -CELL_SIZE
        elif direction == pygame.K_DOWN:
            d_x, d_y = 0, CELL_SIZE

        if d_x or d_y:
            self.rect.move_ip(d_x, d_y)
            if len(pygame.sprite.spritecollide(self, walls, False)):
                self.rect.move_ip(-d_x, -d_y)

    def count_down(self, value):
        self.timer -= value
        if self.timer < 0:
            self.ephemeral = False
            self.timer = 1000
