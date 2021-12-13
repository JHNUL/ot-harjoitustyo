import os
import pygame

from constants import CELL_SIZE
dirname = os.path.dirname(__file__)


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
        self.timer = 20
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "..", "assets", "proto_pac.png")
        )
        self._original_image = pygame.transform.scale(
            self.image, (CELL_SIZE, CELL_SIZE))
        self.image = self._original_image.copy()
        self.damage_image = self.image.copy()
        self.damage_image.set_alpha(128)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, delta_coordinates: tuple, walls: pygame.sprite.Group):
        """Moves Pac

        Args:
            delta_coordinates (tuple): change of x, y coordinates
            walls (pygame.sprite.Group): collection of sprites representing walls in the game
        """
        if delta_coordinates:
            d_x, d_y = delta_coordinates
            self.rect.move_ip(d_x, d_y)
            if len(pygame.sprite.spritecollide(self, walls, False)):
                self.rect.move_ip(-d_x, -d_y)

    def count_down(self):
        """count down the timer and toggle damage image every other tick"""
        self.timer -= 1
        if self.timer % 2 == 0:
            self.image = self.damage_image
        else:
            self.image = self._original_image
        if self.timer <= 0:
            self.ephemeral = False
            self.image = self._original_image
            self.timer = 20
