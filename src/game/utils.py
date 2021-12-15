import os
import re
from random import choice
import pygame
from constants import CELL_SIZE
from game.enums import Direction


def normalize(n: int) -> int:
    return CELL_SIZE * n


def get_random_direction() -> Direction:
    return choice([Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT])


class ImageLoader:
    """static helper class to load and get images"""
    images = {"enemy": []}

    @staticmethod
    def init():
        """Call to load images"""
        image_base_path = os.path.join(
            os.path.dirname(__file__), "..", "assets")
        for image in os.listdir(image_base_path):
            img = pygame.image.load(f"{image_base_path}/{image}")
            if re.match("^enemy.+", image):
                ImageLoader.images["enemy"].append(img)
            else:
                ImageLoader.images[image.split(".")[0]] = img

    @staticmethod
    def get(sprite_name: str) -> pygame.Surface:
        """Get an image for the sprite. For enemies a random image from possible
        choices is returned.

        Args:
            sprite_name (str): name of the sprite

        Returns:
            pygame.Surface: Image as surface object
        """
        img = ImageLoader.images[sprite_name]
        if isinstance(img, list):
            return choice(img)
        return img
