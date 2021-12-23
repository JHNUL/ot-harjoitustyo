import pygame
import constants as const
from game.level import Level


class Renderer:
    """Class that renders the game on the surface"""

    def __init__(self, font, login_menu, game_over_menu, main_screen, game_screen):
        self._login_menu = login_menu
        self._game_over_menu = game_over_menu
        self._font = font
        self._main_screen = main_screen
        self._game_screen = game_screen

    def render(self, level: Level):
        """main render method

        Args:
            level (Level): Level object
        """
        self._game_screen.fill(const.BG_COLOR)
        self._main_screen.fill(const.BG_COLOR)
        self._login_menu.start(self._main_screen)
        if level.is_finished:
            self._game_over_menu.start(self._main_screen)
        player_status = self._font.render(
            const.STATUS.format(level.current_score.value, level.pac.lives), True, const.WHITE)
        top_scores = self._font.render(
            const.LEADERBOARD.format(level.top_scores), True, const.WHITE)
        level.draw(self._game_screen)
        self._main_screen.blit(player_status, (10, 10))
        self._main_screen.blit(top_scores, (10, 40))
        self._main_screen.blit(self._game_screen, (0, const.CELL_SIZE*2))
        pygame.display.flip()
