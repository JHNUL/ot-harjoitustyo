import pygame

BG_COLOR = (25, 51, 77)
WHITE = pygame.Color(255, 255, 255)
CELL_SIZE = 40
MOVE_ENEMIES = pygame.USEREVENT+1

"""Screen titles"""
SCREEN_TITLE_LANDING = "Welcome!"
SCREEN_TITLE_GAME = "PACMAN"
SCREEN_TITLE_GAME_OVER = "Game over!"

"""Screen labels"""
PLAYER_WON = "You Won!"
PLAYER_LOST = "You Lost!"

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

MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

DISPLAY_WIDTH = CELL_SIZE*(len(MAP[0]))
DISPLAY_HEIGHT = CELL_SIZE*(len(MAP)+2)

DIRECTION_KEYS = [pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT]
MOVEMENTS = {
    pygame.K_UP: (0, -CELL_SIZE),
    pygame.K_RIGHT: (CELL_SIZE, 0),
    pygame.K_DOWN: (0, CELL_SIZE),
    pygame.K_LEFT: (-CELL_SIZE, 0)
}
