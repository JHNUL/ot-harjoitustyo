from pygame import Surface
import pygame
from pygame_menu import Menu, events
from game.level import Level
import constants as const


class GameOverMenu:
    def __init__(self, level: Level):
        self.player_lost_screen = Menu(const.SCREEN_TITLE_GAME_OVER, 500, 300)
        self.player_won_screen = Menu(const.SCREEN_TITLE_GAME_OVER, 500, 300)
        self.level = level
        self._init_screens()

    def update(self, evts: list):
        if not self.level.pac.lives:
            self.player_lost_screen.update(evts)
        else:
            self.player_won_screen.update(evts)

    def draw(self, surface: Surface):
        if not self.level.pac.lives:
            self.player_lost_screen.draw(surface)
        else:
            self.player_won_screen.draw(surface)

    def _new_game_callback(self):
        self.level.reset()

    def _init_screens(self):
        self.player_lost_screen.add.label(const.PLAYER_LOST)
        self.player_lost_screen.add.button(
            const.BTN_TEXT_NEW_GAME, self._new_game_callback)
        self.player_lost_screen.add.button(const.BTN_TEXT_QUIT, pygame.QUIT)
        self.player_won_screen.add.label(const.PLAYER_WON)
        self.player_won_screen.add.button(
            const.BTN_TEXT_NEW_GAME, self._new_game_callback)
        self.player_won_screen.add.button(const.BTN_TEXT_QUIT, pygame.QUIT)
