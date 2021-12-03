from random import choice
from constants import CELL_SIZE
from game.enums import Direction


def normalize(n: int) -> int:
    return CELL_SIZE * n


def get_random_direction() -> Direction:
    return choice([Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT])
