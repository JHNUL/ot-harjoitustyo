from pygame_menu import events

import constants as c
from game.menus.screens.base_screen import BaseScreen
from game.menus.screens.screen_names import ScreenName


class LandingScreen(BaseScreen):
    def __init__(self, set_screen):
        super().__init__(c.SCREEN_TITLE_LANDING)
        self._set_screen = set_screen
        self._init_screen()

    def _init_screen(self):
        self.menu.add.button(c.BTN_TEXT_LOGIN, self._login_btn_callback)
        self.menu.add.button(c.BTN_TEXT_CREATE_PLAYER,
                             self._create_player_btn_callback)
        self.menu.add.button(c.BTN_TEXT_QUIT, events.EXIT)

    def _login_btn_callback(self):
        self._set_screen(ScreenName.LOGIN)

    def _create_player_btn_callback(self):
        self._set_screen(ScreenName.CREATE_PLAYER)
