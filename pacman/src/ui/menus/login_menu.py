from pygame import Surface

from models.user import User
from repositories.user_repository import UserRepository
from ui.menus.screens.landing_screen import LandingScreen
from ui.menus.screens.login_screen import LoginScreen
from ui.menus.screens.create_user_screen import CreateUserScreen
from ui.menus.screens.screen_enums import ScreenName


class LoginMenu:
    def __init__(self, player: 'User', user_repository: 'UserRepository'):
        self._player = player
        self._user_repository = user_repository
        self._set_screen(ScreenName.LANDING)

    def _login_callback(self, username):
        user = self._user_repository.find_user(username)
        self._player.set_login_time(user.login_time)
        self._screen.menu.disable()

    def _create_user_callback(self, username, playername):
        print(username, playername)
        self._user_repository.create_user(username, playername)
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
        if self._screen.menu.is_enabled():
            self._screen.draw(surface)
