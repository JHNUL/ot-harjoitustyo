from pygame import Surface
from datetime import datetime

from models.player import Player
from repositories.player_repository import PlayerRepository
from game.menus.screens.landing_screen import LandingScreen
from game.menus.screens.login_screen import LoginScreen
from game.menus.screens.create_player_screen import CreatePlayerScreen
from game.menus.screens.screen_names import ScreenName


class LoginMenu:
    def __init__(self, player: 'Player', player_repository: 'PlayerRepository'):
        self._player = player
        self._player_repository = player_repository
        self._set_screen(ScreenName.LANDING)

    def _login_callback(self, playername):
        player = self._player_repository.find_player_by_name(playername)
        if player is None:
            # TODO: announce in UI that login was unsuccessful
            raise Exception('Player not found')
        player.set_login_time(datetime.now().timestamp())
        res = self._player_repository.set_last_login(player)
        if res:
            self._player.set_player(player)
        self._screen.menu.disable()

    def _create_player_callback(self, playername):
        player = Player(playername=playername)
        self._player_repository.add_player(player)
        self._set_screen(ScreenName.LOGIN)

    def _set_screen(self, screen: ScreenName):
        if screen == ScreenName.LANDING:
            self._screen = LandingScreen(self._set_screen)
        elif screen == ScreenName.CREATE_PLAYER:
            self._screen = CreatePlayerScreen(self._create_player_callback)
        elif screen == ScreenName.LOGIN:
            self._screen = LoginScreen(self._login_callback)
        else:
            raise TypeError(f"{screen} not recognized")

    def update(self, events):
        if self._screen.menu.is_enabled():
            self._screen.update(events)

    def draw(self, surface: 'Surface'):
        if self._screen.menu.is_enabled():
            self._screen.draw(surface)
