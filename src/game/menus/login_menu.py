from pygame import Surface

from models.player import Player
from repositories.player_repository import PlayerRepository
from game.menus.screens.landing_screen import LandingScreen
from game.menus.screens.login_screen import LoginScreen
from game.menus.screens.create_user_screen import CreateUserScreen
from game.menus.screens.screen_enums import ScreenName


class LoginMenu:
    def __init__(self, player: 'Player', player_repository: 'PlayerRepository'):
        self._player = player
        self._player_repository = player_repository
        self._set_screen(ScreenName.LANDING)

    def _login_callback(self, playername):
        player = self._player_repository.find_player(playername)
        self._player.set_player(player)
        self._screen.menu.disable()

    def _create_player_callback(self, playername):
        self._player_repository.create_player(playername)
        self._set_screen(ScreenName.LOGIN)

    def _set_screen(self, screen: ScreenName):
        if screen == ScreenName.LANDING:
            self._screen = LandingScreen(self._set_screen)
        elif screen == ScreenName.CREATE_USER:
            self._screen = CreateUserScreen(self._create_player_callback)
        elif screen == ScreenName.LOGIN:
            self._screen = LoginScreen(self._login_callback)
        else:
            raise TypeError(f"{screen} not recognized")

    def update(self, events):
        self._screen.update(events)

    def draw(self, surface: 'Surface'):
        if self._screen.menu.is_enabled():
            self._screen.draw(surface)
