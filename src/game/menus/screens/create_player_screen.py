from pygame_menu import events

import constants as const
from game.enums import ScreenName
from game.menus.screens.base_screen import BaseScreen


class CreatePlayerScreen(BaseScreen):
    def __init__(self, set_screen, create_player_callback, message=""):
        super().__init__(const.SCREEN_TITLE_CREATE_PLAYER)
        self._create_player_callback = create_player_callback
        self._name = None
        self._set_screen = set_screen
        self._init_screen(message)

    def _set_name(self, value):
        self._name = value

    def _create_player_btn_callback(self):
        self._create_player_callback(self._name)

    def _back_button_callback(self):
        self._set_screen(ScreenName.LANDING)

    def _init_screen(self, message):
        if message:
            self.menu.add.label(message)
        self.menu.add.text_input(
            const.INPUT_LABEL_PLAYER_NAME, onchange=self._set_name)
        self.menu.add.button(const.BTN_TEXT_CREATE_PLAYER,
                             self._create_player_btn_callback)
        self.menu.add.button(const.BTN_TEXT_BACK, self._back_button_callback)
        self.menu.add.button(const.BTN_TEXT_QUIT, events.EXIT)
