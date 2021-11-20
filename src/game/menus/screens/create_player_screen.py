from pygame_menu import events

import constants as c
from game.menus.screens.base_screen import BaseScreen


class CreatePlayerScreen(BaseScreen):
    def __init__(self, create_player_callback):
        super().__init__(c.SCREEN_TITLE_CREATE_PLAYER)
        self._create_player_callback = create_player_callback
        self._playername = None
        self._init_screen()

    def _set_playername(self, value):
        self._playername = value

    def _create_player_btn_callback(self):
        self._create_player_callback(self._playername)

    def _init_screen(self):
        self.menu.add.text_input(
            c.INPUT_LABEL_PLAYERNAME, onchange=self._set_playername)
        self.menu.add.button(c.BTN_TEXT_CREATE_PLAYER,
                             self._create_player_btn_callback)
        self.menu.add.button(c.BTN_TEXT_QUIT, events.EXIT)
