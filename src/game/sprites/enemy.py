from random import choice
import pygame
from game.utils import ImageLoader, get_random_direction
from constants import CELL_SIZE, Direction


class Enemy(pygame.sprite.Sprite):
    """Class containing the logic for enemy

    Attributes:
        image (Surface): the in-game image of the enemy
        rect (Rect): the rectangle of the in-game image
        vulnerable (bool): if enemy is vulnerable
        direction (Direction): one of four possible directions in the game
    """

    def __init__(self, x: int, y: int):
        """Constructor

        Args:
            x (int): starting x coordinate for the enemy
            y (int): starting y coordinate for the enemy
        """
        super().__init__()
        self.image = pygame.transform.scale(
            ImageLoader.get("enemy"), (CELL_SIZE, CELL_SIZE))
        self.image = pygame.transform.scale(
            self.image, (CELL_SIZE, CELL_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.timer = 60
        self.vulnerable = False
        self.direction = get_random_direction()

    def _can_move(self, walls: pygame.sprite.Group, x: int, y: int) -> bool:
        """Method to check if enemy can move to given x and y position

        Args:
            walls (pygame.sprite.Group): collection of sprites representing walls in the game
            x (int): x coordinate to move
            y (int): y coordinate to move

        Returns:
            bool: True if can move
        """
        can = True
        self.rect.move_ip(x, y)
        if len(pygame.sprite.spritecollide(self, walls, False)):
            can = False
        self.rect.move_ip(-x, -y)
        return can

    def _get_allowed_directions(self, walls: pygame.sprite.Group) -> list:
        """Get possible directions where the enemy can move to. Directions are represented as enum.

        Args:
            walls (pygame.sprite.Group): collection of sprites representing walls in the game

        Returns:
            list: List of possible directions
        """
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

    def move(self, walls: pygame.sprite.Group, direction: Direction = None):
        """Moves enemy to somewhat random direction unless direction is given as argument.

        Args:
            walls (pygame.sprite.Group): collection of sprites representing walls in the game
            direction (Direction, optional): direction to move enemy. Defaults to None.
        """
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

    def set_vulnerable(self):
        self.vulnerable = True
        self.image.set_alpha(128)

    def count_down(self):
        """count down the timer, when zero reset timer and set original image"""
        self.timer -= 1
        if self.timer <= 0:
            self.vulnerable = False
            self.image.set_alpha(255)
            self.timer = 60
