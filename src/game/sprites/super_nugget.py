import pygame

from constants import CELL_SIZE
from game.utils import ImageLoader


class SuperNugget(pygame.sprite.Sprite):
    """Class containing the logic for super nugget

    Attributes:
        image (Surface): the in-game image of the nugget
        rect (Rect): the rectangle of the in-game image
    """

    def __init__(self, x: int, y: int):
        """Constructor

        Args:
            x (int): x coordinate
            y (int): y coordinate
        """
        super().__init__()

        self.image = ImageLoader.get("super_nugget")
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
