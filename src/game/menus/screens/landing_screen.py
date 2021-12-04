import pygame

import constants as const
from game.enums import ScreenName
from game.menus.screens.base_screen import BaseScreen


class LandingScreen(BaseScreen):
    def __init__(self, set_screen):
        super().__init__(const.SCREEN_TITLE_LANDING)
        self._set_screen = set_screen
        self._init_screen()

    def _init_screen(self):
        self.menu.add.button(const.BTN_TEXT_LOGIN, self._login_btn_callback)
        self.menu.add.button(const.BTN_TEXT_CREATE_PLAYER,
                             self._create_player_btn_callback)
        self.menu.add.button(const.BTN_TEXT_QUIT, pygame.QUIT)

    def _login_btn_callback(self):
        self._set_screen(ScreenName.LOGIN)

    def _create_player_btn_callback(self):
        self._set_screen(ScreenName.CREATE_PLAYER)
