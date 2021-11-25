from pygame_menu import events

import constants as c
from game.menus.screens.base_screen import BaseScreen


class LoginScreen(BaseScreen):
    def __init__(self, login_callback, message=""):
        super().__init__(c.SCREEN_TITLE_LOGIN)
        self._login_callback = login_callback
        self._playername = None
        self._init_screen(message)

    def _login_btn_callback(self):
        self._login_callback(self._playername)

    def _set_playername(self, value):
        self._playername = value

    def _init_screen(self, message):
        if message:
            self.menu.add.label(message)
        self.menu.add.text_input(
            c.INPUT_LABEL_PLAYERNAME, onchange=self._set_playername)
        self.menu.add.button(c.BTN_TEXT_LOGIN, self._login_btn_callback)
        self.menu.add.button(c.BTN_TEXT_QUIT, events.EXIT)
