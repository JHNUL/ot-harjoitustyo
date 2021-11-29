from pygame_menu import events

import constants as const
from game.menus.screens.base_screen import BaseScreen
from game.menus.screens.screen_names import ScreenName


class LoginScreen(BaseScreen):
    def __init__(self, set_screen, login_callback, message=""):
        super().__init__(const.SCREEN_TITLE_LOGIN)
        self._login_callback = login_callback
        self._name = None
        self._set_screen = set_screen
        self._init_screen(message)

    def _login_btn_callback(self):
        self._login_callback(self._name)

    def _set_name(self, value):
        self._name = value

    def _back_button_callback(self):
        self._set_screen(ScreenName.LANDING)

    def _init_screen(self, message):
        if message:
            self.menu.add.label(message)
        self.menu.add.text_input(
            const.INPUT_LABEL_PLAYER_NAME, onchange=self._set_name)
        self.menu.add.button(const.BTN_TEXT_LOGIN, self._login_btn_callback)
        self.menu.add.button(const.BTN_TEXT_BACK, self._back_button_callback)
        self.menu.add.button(const.BTN_TEXT_QUIT, events.EXIT)
