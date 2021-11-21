import pygame
from constants import BG_COLOR, DISPLAY_HEIGHT, DISPLAY_WIDTH, SCREEN_TITLE_GAME
from models.player import Player
from game.sprites.pac import Pac
from game.menus.login_menu import LoginMenu
from repositories.player_repository import PlayerRepository
from db_connection import get_db_connection
from init_db import initialize


def main():
    initialize()
    pygame.init()
    surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption(SCREEN_TITLE_GAME)
    player = Player()
    login_menu = LoginMenu(player, PlayerRepository(get_db_connection()))
    clock = pygame.time.Clock()
    sprites = pygame.sprite.Group()
    sprites.add(Pac())
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        surface.fill(BG_COLOR)

        if player.last_login is None:
            login_menu.update(events)
            login_menu.draw(surface)
            pygame.display.flip()
            continue

        sprites.draw(surface)
        pygame.display.flip()
        clock.tick(15)


if __name__ == "__main__":
    main()
