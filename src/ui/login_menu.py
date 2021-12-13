from pygame import Surface, event
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
        self._name = None
        self._init_screen()

    def _start_btn_callback(self):
        """Callback for start button"""
        player = self._player_service.player_login(self._name)
        self._player.set_player(player)
        self._score.set_player_id(player)
        self._menu.disable()

    def _quit_game_callback(self):
        """Callback for quit game button"""
        self._menu.disable()
        quit_event = event.Event(const.QUIT_EVENT)
        event.post(quit_event)

    def _set_name(self, value: str):
        """Set the name from input

        Args:
            value (str): input from ui component
        """
        self._name = value

    def _init_screen(self):
        """Initializes the menu with buttons and input"""
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
