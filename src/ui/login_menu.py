import re
from pygame import Surface, event, Color
from pygame_menu import Menu

import constants as const
from models.player import Player
from models.score import Score
from services.player_service import PlayerService


class LoginMenu:
    """Class that holds the UI for login menu which is shown on game start"""

    def __init__(self, player: Player, player_service: PlayerService, score: Score):
        """Constructor

        Args:
            player (Player): Player object
            player_service (PlayerService): Playerservice object
            score (Score): Score object
        """
        self._menu = Menu(const.SCREEN_TITLE_LANDING, 500, 300)
        self._player = player
        self._score = score
        self._player_service = player_service
        self._name = ""
        self._start_disabled = True
        self._label = None
        self._error_label = None
        self._init_screen()

    def _start_btn_callback(self):
        if not self._start_disabled:
            player = self._player_service.player_login(self._name)
            if player is not None:
                self._player.set_player(player)
                self._score.set_player_id(player)
                self._menu.disable()
            else:
                self._error_label.show()
        else:
            self._label.show()

    def _quit_game_callback(self):
        quit_event = event.Event(const.QUIT_EVENT)
        event.post(quit_event)
        self._menu.disable()

    def _set_name(self, value: str):
        if not re.match("^([a-zA-Z0-9]){1,10}$", value):
            self._label.show()
            self._start_disabled = True
        else:
            self._label.hide()
            self._start_disabled = False
        self._name = value

    def _init_screen(self):
        self._label = self._menu.add.label(const.NAME_INPUT_WARNING)
        self._label.add_underline(Color(255, 0, 0), 0, 2)
        self._label.resize(240, 30)
        self._label.hide()
        self._error_label = self._menu.add.label(const.LOGIN_FAILED)
        self._error_label.add_underline(Color(255, 0, 0), 0, 2)
        self._error_label.resize(240, 30)
        self._error_label.hide()
        self._menu.add.text_input(
            const.INPUT_LABEL_PLAYER_NAME, onchange=self._set_name)
        self._menu.add.button(
            const.BTN_TXT_START, self._start_btn_callback)
        self._menu.add.button(const.BTN_TEXT_QUIT, self._quit_game_callback)

    def start(self, surface: Surface):
        """Starts the menu main loop

        Args:
            surface (Surface): pygame Surface object
        """
        if self._menu.is_enabled():
            self._menu.mainloop(surface)
