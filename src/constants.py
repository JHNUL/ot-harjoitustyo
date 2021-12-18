from functools import total_ordering
from enum import Enum
import pygame


@total_ordering
class Direction(Enum):
    """Enumerated types to represent direction"""
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


BG_COLOR = (25, 51, 77)
WHITE = pygame.Color(255, 255, 255)
CELL_SIZE = 40
ENEMY_MOVE_INTERVAL = 300
MOVE_ENEMIES = pygame.USEREVENT+1
MOVE_VULNERABLE_ENEMIES = pygame.USEREVENT+2
QUIT_EVENT = pygame.USEREVENT+3
PAC_CHANGE_MOUTH = pygame.USEREVENT+4

"""Screen titles"""
SCREEN_TITLE_LANDING = "Welcome!"
SCREEN_TITLE_GAME = "PACMAN"
SCREEN_TITLE_GAME_OVER = "Game over!"

"""Screen labels"""
PLAYER_WON = "You Won!"
PLAYER_LOST = "You Lost!"
PLAYER_SCORE = "Your score was: {}, placing: {}."

"""Button texts"""
BTN_TXT_START = "Start"
BTN_TEXT_NEW_GAME = "New game"
BTN_TEXT_QUIT = "Quit"

"""Text input labels"""
INPUT_LABEL_PLAYER_NAME = "Player name:"

"""Environment"""
PRODUCTION = "prod"
TESTING = "test"
DEVELOPMENT = "dev"


DIRECTION_KEYS = [pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT]
DIRECTION_MAP = {
    pygame.K_UP: Direction.UP,
    pygame.K_RIGHT: Direction.RIGHT,
    pygame.K_DOWN: Direction.DOWN,
    pygame.K_LEFT: Direction.LEFT
}
MOVEMENTS = {
    Direction.UP: (0, -CELL_SIZE),
    Direction.RIGHT: (CELL_SIZE, 0),
    Direction.DOWN: (0, CELL_SIZE),
    Direction.LEFT: (-CELL_SIZE, 0)
}

# disabling rule because it is important to see the map in its full width when changing something
# pylint: disable=line-too-long
MAP = [
    [6,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5, 14,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  7],
    [1,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  4,  1],
    [1,  0, 10, 11,  0, 10,  5,  5,  5,  5,  5,  5,  5,  5, 11,  0, 12,  0, 10,  5,  5,  5,  5,  5,  5,  5,  5, 11,  0, 10, 11,  0,  1],
    [1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
    [1,  0,  6,  7,  0, 10,  5,  5, 14,  5,  5,  5, 11,  0, 10,  5, 14,  5, 11,  0, 10,  5,  5,  5, 14,  5,  5, 11,  0,  6,  7,  0,  1],
    [1,  0,  9,  8,  0,  0,  0,  0, 12,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0, 12,  0,  0,  0,  0,  9,  8,  0,  1],
    [1,  0,  0,  0,  0, 13,  0,  0,  0,  0,  0,  0, 13,  0,  0,  0, 12,  0,  0,  0, 13,  0,  0,  0,  0,  0,  0, 13,  0,  0,  0,  0,  1],
    [1,  0,  6,  7,  0,  1,  0, 10,  5,  5,  5,  5,  8,  0,  0,  0,  0,  0,  0,  0,  9,  5,  5,  5,  5, 11,  0,  1,  0,  6,  7,  0,  1],
    [1,  0,  9,  8,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0, 13,  0,  0,  0, 13,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  9,  8,  0,  1],
    [1,  0,  0,  0,  0,  9,  5,  5,  5,  5,  5,  5, 11,  0,  1,  3,  3,  3,  1,  0, 10,  5,  5,  5,  5,  5,  5,  8,  0,  0,  0,  0,  1],
    [1,  0,  6,  7,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  3,  3,  3,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  6,  7,  0,  1],
    [1,  0,  1,  1,  0, 10,  5, 11,  0, 10,  5,  5, 11,  0,  9,  5,  5,  5,  8,  0, 10,  5,  5, 11,  0, 10,  5, 11,  0,  1,  1,  0,  1],
    [1,  0,  9,  8,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  9,  8,  0,  1],
    [1,  0,  0,  0,  0, 10,  5,  5, 11,  0, 10,  5,  5,  5, 11,  0, 13,  0, 10,  5,  5,  5, 11,  0, 10,  5,  5, 11,  0,  0,  0,  0,  1],
    [1,  0,  6,  7,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  6,  7,  0,  1],
    [1,  0,  9,  8,  0, 10,  5, 11,  0, 10,  5,  5, 11,  0, 10,  5, 15,  5, 11,  0, 10,  5,  5, 11,  0, 10,  5, 11,  0,  9,  8,  0,  1],
    [1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
    [1,  0, 10, 11,  0, 10,  5,  5,  5,  5,  5,  5,  5,  5, 11,  0, 13,  0, 10,  5,  5,  5,  5,  5,  5,  5,  5, 11,  0, 10, 11,  0,  1],
    [1,  4,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  4,  1],
    [9,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5, 15,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  8]
]

DISPLAY_WIDTH = CELL_SIZE*(len(MAP[0]))
DISPLAY_HEIGHT = CELL_SIZE*(len(MAP)+2)
