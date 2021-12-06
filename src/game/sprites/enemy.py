import os
from random import choice
import pygame
from constants import CELL_SIZE
from game.enums import Direction
from utils import get_random_direction

dirname = os.path.dirname(__file__)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "..", "assets", "proto_enemy.png")
        )
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = get_random_direction()

    def _can_move(self, walls, x, y):
        can = True
        self.rect.move_ip(x, y)
        if len(pygame.sprite.spritecollide(self, walls, False)):
            can = False
        self.rect.move_ip(-x, -y)
        return can

    def _get_allowed_directions(self, walls) -> list:
        allowed_dirs = {
            Direction.UP: True,
            Direction.RIGHT: True,
            Direction.DOWN: True,
            Direction.LEFT: True
        }
        if self.direction == Direction.UP:
            allowed_dirs[Direction.DOWN] = False
        elif self.direction == Direction.RIGHT:
            allowed_dirs[Direction.LEFT] = False
        elif self.direction == Direction.DOWN:
            allowed_dirs[Direction.UP] = False
        elif self.direction == Direction.LEFT:
            allowed_dirs[Direction.RIGHT] = False

        if allowed_dirs[Direction.UP]:
            allowed_dirs[Direction.UP] = self._can_move(walls, 0, -CELL_SIZE)
        if allowed_dirs[Direction.RIGHT]:
            allowed_dirs[Direction.RIGHT] = self._can_move(walls, CELL_SIZE, 0)
        if allowed_dirs[Direction.DOWN]:
            allowed_dirs[Direction.DOWN] = self._can_move(walls, 0, CELL_SIZE)
        if allowed_dirs[Direction.LEFT]:
            allowed_dirs[Direction.LEFT] = self._can_move(walls, -CELL_SIZE, 0)

        return [x[0] for x in allowed_dirs.items() if x[1]]

    def move(self, walls, direction: Direction = None):

        self.direction = direction if direction else choice(
            self._get_allowed_directions(walls))

        d_x, d_y = 0, 0
        if self.direction == Direction.LEFT:
            d_x, d_y = -CELL_SIZE, 0
        elif self.direction == Direction.RIGHT:
            d_x, d_y = CELL_SIZE, 0
        elif self.direction == Direction.UP:
            d_x, d_y = 0, -CELL_SIZE
        elif self.direction == Direction.DOWN:
            d_x, d_y = 0, CELL_SIZE

        self.rect.move_ip(d_x, d_y)

        if len(pygame.sprite.spritecollide(self, walls, False)):
            self.rect.move_ip(-d_x, -d_y)
