from pygame import Surface, event
from pygame_menu import Menu
from game.level import Level
import constants as const
from services.score_service import ScoreService


class GameOverMenu:
    """Class that holds the UI for game over menu"""

    def __init__(self, level: Level, score_service: ScoreService):
        """Constructor

        Args:
            level (Level): Level object
            score_service (ScoreService): Score service
        """
        self._menu = Menu(const.SCREEN_TITLE_GAME_OVER, 500, 300)
        self._label = None
        self._score_label = None
        self._level = level
        self._score_service = score_service
        self._init_screens()

    def _new_game_callback(self):
        self._score_label.hide()
        self._menu.disable()
        self._level.reset()

    def _quit_game_callback(self):
        self._menu.disable()
        quit_event = event.Event(const.QUIT_EVENT)
        event.post(quit_event)

    def _init_screens(self):
        self._label = self._menu.add.label("")
        self._score_label = self._menu.add.label("")
        self._score_label.hide()
        self._menu.add.button(
            const.BTN_TEXT_NEW_GAME, self._new_game_callback)
        self._menu.add.button(const.BTN_TEXT_QUIT, self._quit_game_callback)

    def start(self, surface: Surface):
        """Starts the menu main loop

        Args:
            surface (Surface): pygame Surface object
        """
        self._menu.enable()
        if self._level.pac.lives:
            title = const.PLAYER_WON
            rank = self._score_service.get_rank_of_score_by_id(self._level.current_score.id)
            if rank is not None:
                self._score_label.set_title(
                    const.PLAYER_SCORE.format(self._level.current_score.value, rank))
            else:
                self._score_label.set_title("Error saving score")
            self._score_label.show()
        else:
            title = const.PLAYER_LOST
        self._label.set_title(title)
        self._menu.mainloop(surface)
