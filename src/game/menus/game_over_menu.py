from pygame import Surface, QUIT
from pygame_menu import Menu
from game.level import Level
import constants as const


class GameOverMenu:
    """Class that holds the UI for game over menu"""

    def __init__(self, level: Level):
        """Constructor

        Args:
            level (Level): Level object
        """
        self._menu = Menu(const.SCREEN_TITLE_GAME_OVER, 500, 300)
        self._label = None
        self._level = level
        self._init_screens()

    def _new_game_callback(self):
        """Callback for new game button"""
        self._menu.disable()
        self._level.reset()

    def _init_screens(self):
        """Initializes the menu with buttons and label"""
        self._label = self._menu.add.label("")
        self._menu.add.button(
            const.BTN_TEXT_NEW_GAME, self._new_game_callback)
        self._menu.add.button(const.BTN_TEXT_QUIT, QUIT)

    def start(self, surface: Surface):
        """Starts the menu main loop

        Args:
            surface (Surface): pygame Surface object
        """
        self._menu.enable()
        title = const.PLAYER_WON if self._level.pac.lives else const.PLAYER_LOST
        self._label.set_title(title)
        self._menu.mainloop(surface)
