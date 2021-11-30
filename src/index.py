import sys
import pygame
from constants import BG_COLOR, SCREEN_TITLE_GAME, WHITE
from game.level import Level
from game.menus.game_over_menu import GameOverMenu
from game.menus.login_menu import LoginMenu
from models.score import Score
from models.player import Player
from repositories.player_repository import PlayerRepository
from db_connection import get_db_connection
from init_db import initialize_db
from utils import normalize

MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 3, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


def main():
    initialize_db()
    pygame.init()

    display_width = normalize(len(MAP[0]))
    display_height = normalize(len(MAP))
    surface = pygame.display.set_mode((display_width, display_height))
    game_surface = pygame.Surface((display_width, display_height-50))
    pygame.display.set_caption(SCREEN_TITLE_GAME)

    player = Player()
    score = Score(0)
    level = Level(MAP, score)
    login_menu = LoginMenu(player, PlayerRepository(get_db_connection()))
    game_over_menu = GameOverMenu(level)
    clock = pygame.time.Clock()
    direction = None
    font = pygame.font.SysFont(None, 32)

    while True:
        game_surface.fill(BG_COLOR)
        surface.fill(BG_COLOR)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT]:
                    direction = event.key
            if event.type == pygame.KEYUP:
                direction = None

        if player.last_login is None:
            login_menu.update(events)
            login_menu.draw(surface)
            pygame.display.flip()
            continue

        if not level.pac.lives:
            game_over_menu.update(events)
            game_over_menu.draw(surface)
            pygame.display.flip()
            continue

        if direction:
            level.move_pac(direction)

        txt = font.render(
            f"SCORE: {level.current_score.value}, LIVES: {level.pac.lives}", True, WHITE)
        level.sprites.draw(game_surface)
        surface.blit(txt, (20, 20))
        surface.blit(game_surface, (0, 50))
        pygame.display.flip()
        clock.tick(10)


if __name__ == "__main__":
    main()
