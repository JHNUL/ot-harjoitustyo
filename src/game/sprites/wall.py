import pygame

from constants import CELL_SIZE
from game.utils import ImageLoader


class Wall(pygame.sprite.Sprite):
    """Class containing the logic for wall

    Attributes:
        image (Surface): the in-game image of the nugget
        rect (Rect): the rectangle of the in-game image
    """

    def __init__(self, x: int, y: int, model: int):
        """Constructor

        Args:
            x (int): x coordinate
            y (int): y coordinate
        """
        super().__init__()
        name = "wall_vertical"
        if model == 5:
            name = "wall_horizontal"
        if model == 6:
            name = "wall_angle_upper_left"
        if model == 7:
            name = "wall_angle_upper_right"
        if model == 8:
            name = "wall_angle_lower_right"
        if model == 9:
            name = "wall_angle_lower_left"
        if model == 10:
            name = "wall_end_left"
        if model == 11:
            name = "wall_end_right"
        if model == 12:
            name = "wall_end_down"
        if model == 13:
            name = "wall_end_up"
        if model == 14:
            name = "wall_tee_down"
        if model == 15:
            name = "wall_tee_up"
        self.image = ImageLoader.get(name)
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
