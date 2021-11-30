from pygame import Surface
from pygame_menu import Menu, events
from game.level import Level
import constants as const


class GameOverMenu:
    def __init__(self, level: Level):
        self.menu = Menu(const.SCREEN_TITLE_GAME_OVER, 500, 300)
        self.level = level
        self._init_screen()

    def update(self, evts: list):
        self.menu.update(evts)

    def draw(self, surface: Surface):
        self.menu.draw(surface)

    def _new_game_callback(self):
        self.level.create_level()

    def _init_screen(self):
        self.menu.add.button(const.BTN_TEXT_NEW_GAME, self._new_game_callback)
        self.menu.add.button(const.BTN_TEXT_QUIT, events.EXIT)
