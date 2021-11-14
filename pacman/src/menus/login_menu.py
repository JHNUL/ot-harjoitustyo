from pygame import Surface

from user import User
from menus.screens.landing_screen import LandingScreen
from menus.screens.login_screen import LoginScreen
from menus.screens.create_user_screen import CreateUserScreen
from menus.screens.screen_enums import ScreenName


class LoginMenu:
    def __init__(self, player: 'User'):
        self._player = player
        self._set_screen(ScreenName.LANDING)

    def _login_callback(self, username):
        print("login callback")
        print(username)

    def _create_user_callback(self, username, playername):
        print("create user callback")
        print(username)
        print(playername)
        self._set_screen(ScreenName.LOGIN)

    def _set_screen(self, screen: ScreenName):
        if screen == ScreenName.LANDING:
            self._screen = LandingScreen(self._set_screen)
        elif screen == ScreenName.CREATE_USER:
            self._screen = CreateUserScreen(self._create_user_callback)
        elif screen == ScreenName.LOGIN:
            self._screen = LoginScreen(self._login_callback)
        else:
            raise TypeError(f"{screen} not recognized")

    def update(self, events):
        self._screen.update(events)

    def draw(self, surface: 'Surface'):
        self._screen.draw(surface)
