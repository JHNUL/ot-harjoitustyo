from enum import Enum


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


class ScreenName(Enum):
    LANDING = 'LANDING'
    LOGIN = 'LOGIN'
    CREATE_PLAYER = 'CREATE_PLAYER'
