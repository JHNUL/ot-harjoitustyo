import pygame
from constants import CELL_SIZE, DISPLAY_HEIGHT, DISPLAY_WIDTH, MAP, SCREEN_TITLE_GAME, MOVE_ENEMIES
from game.level import Level
from game.menus.game_over_menu import GameOverMenu
from game.menus.login_menu import LoginMenu
from main_loop import MainLoop
from models.score import Score
from models.player import Player
from renderer import Renderer
from repositories.player_repository import PlayerRepository
from repositories.score_repository import ScoreRepository
from db_connection import get_db_connection
from init_db import initialize_db
from services.player_service import PlayerService
from services.score_service import ScoreService


def main():
    pygame.init()
    pygame.display.set_caption(SCREEN_TITLE_GAME)
    pygame.time.set_timer(MOVE_ENEMIES, 300)
    main_screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    game_screen = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT-CELL_SIZE*2))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Segoe', 34)

    player = Player()
    score = Score(0)
    player_repository = PlayerRepository(get_db_connection())
    score_repository = ScoreRepository(get_db_connection())
    player_service = PlayerService(player_repository=player_repository)
    score_service = ScoreService(score_repository=score_repository)
    level = Level(level_map=MAP, score=score, score_service=score_service)
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
