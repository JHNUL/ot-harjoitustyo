from pygame import Surface, QUIT
from pygame_menu import Menu

import constants as const
from models.player import Player
from models.score import Score
from services.player_service import PlayerService


class LoginMenu:
    def __init__(self, player: Player, player_service: PlayerService, score: Score):
        self._menu = Menu(const.SCREEN_TITLE_LANDING, 500, 300)
        self._player = player
        self._score = score
        self._player_service = player_service
        self._name = None
        self._init_screen()

    def _start_btn_callback(self):
        player = self._player_service.player_login(self._name)
        self._player.set_player(player)
        self._score.set_player_id(player)
        self._menu.disable()

    def _set_name(self, value: str):
        self._name = value

    def _init_screen(self):
        self._menu.add.text_input(
            const.INPUT_LABEL_PLAYER_NAME, onchange=self._set_name)
        self._menu.add.button(
            const.BTN_TXT_START, self._start_btn_callback)
        self._menu.add.button(const.BTN_TEXT_QUIT, QUIT)

    def start(self, surface: Surface):
        if self._menu.is_enabled():
            self._menu.mainloop(surface)
