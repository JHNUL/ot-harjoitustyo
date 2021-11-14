from pygame_menu import events

import constants as c
from ui.menus.screens.base_screen import BaseScreen


class LoginScreen(BaseScreen):
    def __init__(self, login_callback):
        super().__init__(c.SCREEN_TITLE_LOGIN)
        self._login_callback = login_callback
        self._username = None
        self._init_screen()

    def _login_btn_callback(self):
        self._login_callback(self._username)

    def _set_username(self, value):
        self._username = value

    def _init_screen(self):
        self.menu.add.text_input(
            c.INPUT_LABEL_USERNAME, onchange=self._set_username)
        self.menu.add.button(c.BTN_TEXT_LOGIN, self._login_btn_callback)
        self.menu.add.button(c.BTN_TEXT_QUIT, events.EXIT)
