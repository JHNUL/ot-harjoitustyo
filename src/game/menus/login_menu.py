from datetime import datetime
from sqlite3 import IntegrityError
from pygame import Surface
from constants import PLAYER_ALREADY_EXISTS, PLAYER_NOT_FOUND

from models.player import Player
from repositories.player_repository import PlayerRepository
from game.menus.screens.landing_screen import LandingScreen
from game.menus.screens.login_screen import LoginScreen
from game.menus.screens.create_player_screen import CreatePlayerScreen
from game.menus.screens.screen_names import ScreenName


class LoginMenu:
    def __init__(self, player: Player, player_repository: PlayerRepository):
        self._player = player
        self._player_repository = player_repository
        self._set_screen(ScreenName.LANDING)

    def _login_callback(self, name):
        player = self._player_repository.find_player_by_name(name)
        if player is None:
            self._set_screen(ScreenName.LOGIN, PLAYER_NOT_FOUND.format(name))
            return
        player.set_login_time(datetime.now().timestamp())
        res = self._player_repository.set_last_login(player)
        if res:
            self._player.set_player(player)

    def _create_player_callback(self, name):
        player = Player(name=name)
        try:
            self._player_repository.add_player(player)
        except IntegrityError:
            self._set_screen(ScreenName.CREATE_PLAYER,
                             PLAYER_ALREADY_EXISTS.format(name))
            return
        self._set_screen(ScreenName.LOGIN)

    def _set_screen(self, screen: ScreenName, message=""):
        if screen == ScreenName.LANDING:
            self._screen = LandingScreen(self._set_screen)
        elif screen == ScreenName.CREATE_PLAYER:
            self._screen = CreatePlayerScreen(
                self._set_screen, self._create_player_callback, message)
        elif screen == ScreenName.LOGIN:
            self._screen = LoginScreen(
                self._set_screen, self._login_callback, message)
        else:
            raise TypeError(f"{screen} not recognized")

    def update(self, events):
        if self._screen.menu.is_enabled():
            self._screen.update(events)

    def draw(self, surface: Surface):
        if self._screen.menu.is_enabled():
            self._screen.draw(surface)
