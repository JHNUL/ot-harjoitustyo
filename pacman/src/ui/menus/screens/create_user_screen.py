from pygame_menu import events

import constants as c
from ui.menus.screens.base_screen import BaseScreen


class CreateUserScreen(BaseScreen):
    def __init__(self, create_user_callback):
        super().__init__(c.SCREEN_TITLE_CREATE_USER)
        self._create_user_callback = create_user_callback
        self._username = None
        self._playername = None
        self._init_screen()

    def _set_username(self, value):
        self._username = value

    def _set_playername(self, value):
        self._playername = value

    def _create_user_btn_callback(self):
        print(f"Create user pressed {self._username} {self._playername}")
        # handle user creation
        self._create_user_callback(self._username, self._playername)

    def _init_screen(self):
        self.menu.add.text_input(
            c.INPUT_LABEL_USERNAME, onchange=self._set_username)
        self.menu.add.text_input(
            c.INPUT_LABEL_PLAYERNAME, onchange=self._set_playername)
        self.menu.add.button(c.BTN_TEXT_CREATE_USER,
                             self._create_user_btn_callback)
        self.menu.add.button(c.BTN_TEXT_QUIT, events.EXIT)
