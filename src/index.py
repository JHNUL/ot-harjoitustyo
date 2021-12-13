import pygame
import constants as const
from game.level import Level
from game.main_loop import MainLoop
from ui.game_over_menu import GameOverMenu
from ui.login_menu import LoginMenu
from ui.renderer import Renderer
from models.score import Score
from models.player import Player
from repositories.player_repository import PlayerRepository
from repositories.score_repository import ScoreRepository
from db_connection import get_db_connection
from init_db import initialize_db
from services.player_service import PlayerService
from services.score_service import ScoreService


def main():
    pygame.init()
    pygame.display.set_caption(const.SCREEN_TITLE_GAME)
    pygame.time.set_timer(const.MOVE_ENEMIES, const.ENEMY_MOVE_INTERVAL)
    pygame.time.set_timer(const.MOVE_VULNERABLE_ENEMIES,
                          const.ENEMY_MOVE_INTERVAL//2)
    main_screen = pygame.display.set_mode(
        (const.DISPLAY_WIDTH, const.DISPLAY_HEIGHT))
    game_screen = pygame.Surface(
        (const.DISPLAY_WIDTH, const.DISPLAY_HEIGHT-const.CELL_SIZE*2))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Segoe', 34)

    player = Player()
    score = Score(0)
    player_repository = PlayerRepository(get_db_connection())
    score_repository = ScoreRepository(get_db_connection())
    player_service = PlayerService(player_repository=player_repository)
    score_service = ScoreService(score_repository=score_repository)
    level = Level(level_map=const.MAP, score=score,
                  score_service=score_service)
    login_menu = LoginMenu(
        player=player, player_service=player_service, score=score)
    game_over_menu = GameOverMenu(level)
    renderer = Renderer(
        level=level,
        font=font,
        login_menu=login_menu,
        game_over_menu=game_over_menu,
        main_screen=main_screen,
        game_screen=game_screen
    )
    game_loop = MainLoop(level=level, renderer=renderer, clock=clock)
    game_loop.start()
    pygame.display.quit()
    pygame.quit()


if __name__ == "__main__":
    initialize_db()
    main()
