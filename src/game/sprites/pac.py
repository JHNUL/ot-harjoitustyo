import pygame

from constants import CELL_SIZE, MOVEMENTS, Direction
from game.utils import ImageLoader


class Pac(pygame.sprite.Sprite):
    """Class containing the logic for Pac

    Attributes:
        lives (int): how many lives Pac has left
        ephemeral (bool): when True, Pac is invulnerable but cannot consume nuggets
        timer (int): countdown time to return to normal state
        image (Surface): the in-game image of the Pac
        damage_image (Surface): image when Pac has taken damage
        rect (Rect): the rectangle of the in-game image
    """

    def __init__(self, x: int, y: int):
        super().__init__()
        self.lives = 3
        self.ephemeral = False
        self._is_mouth_open = True
        self._orientation = Direction.RIGHT  # now hardcoded starting position
        self.timer = 15
        self.image_open_right = pygame.transform.scale(
            ImageLoader.get("pac_mouth_open_r"), (CELL_SIZE, CELL_SIZE))
        self.image_open_down = pygame.transform.scale(
            ImageLoader.get("pac_mouth_open_d"), (CELL_SIZE, CELL_SIZE))
        self.image_open_left = pygame.transform.scale(
            ImageLoader.get("pac_mouth_open_l"), (CELL_SIZE, CELL_SIZE))
        self.image_open_up = pygame.transform.scale(
            ImageLoader.get("pac_mouth_open_u"), (CELL_SIZE, CELL_SIZE))
        self.image_closed_right = pygame.transform.scale(
            ImageLoader.get("pac_mouth_closed_r"), (CELL_SIZE, CELL_SIZE))
        self.image_closed_down = pygame.transform.scale(
            ImageLoader.get("pac_mouth_closed_d"), (CELL_SIZE, CELL_SIZE))
        self.image_closed_left = pygame.transform.scale(
            ImageLoader.get("pac_mouth_closed_l"), (CELL_SIZE, CELL_SIZE))
        self.image_closed_up = pygame.transform.scale(
            ImageLoader.get("pac_mouth_closed_u"), (CELL_SIZE, CELL_SIZE))
        self.images = [
            self.image_open_right,
            self.image_open_down,
            self.image_open_left,
            self.image_open_up,
            self.image_closed_right,
            self.image_closed_down,
            self.image_closed_left,
            self.image_closed_up
        ]
        self.image = self.image_open_right
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, direction: int, walls: pygame.sprite.Group):
        """Moves Pac

        Args:
            delta_coordinates (tuple): change of x, y coordinates
            walls (pygame.sprite.Group): collection of sprites representing walls in the game
        """
        if direction:
            did_move = True
            d_x, d_y = MOVEMENTS[direction]
            self.rect.move_ip(d_x, d_y)
            if len(pygame.sprite.spritecollide(self, walls, False)):
                self.rect.move_ip(-d_x, -d_y)
                did_move = False
            if did_move and direction != self._orientation:
                self._resolve_image(direction)
                self._orientation = direction

    def _resolve_image(self, direction: Direction):
        if direction == Direction.RIGHT:
            self.image = self.image_open_right if self._is_mouth_open else self.image_closed_right
        elif direction == Direction.DOWN:
            self.image = self.image_open_down if self._is_mouth_open else self.image_closed_down
        elif direction == Direction.LEFT:
            self.image = self.image_open_left if self._is_mouth_open else self.image_closed_left
        elif direction == Direction.UP:
            self.image = self.image_open_up if self._is_mouth_open else self.image_closed_up
        x = self.rect.x
        y = self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def count_down(self):
        """count down the timer to become normal"""
        self.timer -= 1
        if self.timer <= 0:
            self.ephemeral = False
            for image in self.images:
                image.set_alpha(255)
            self.timer = 15

    def set_ephemeral(self):
        self.ephemeral = True
        for image in self.images:
            image.set_alpha(100)

    def change_mouth(self):
        """Change pac image to make mouth open and close"""
        self._is_mouth_open = not self._is_mouth_open
        self._resolve_image(self._orientation)
