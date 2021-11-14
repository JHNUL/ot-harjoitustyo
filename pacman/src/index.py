import pygame
from constants import DISPLAY_HEIGHT, DISPLAY_WIDTH
from menus.login_menu import LoginMenu
from user import User


def main():
    pygame.init()
    surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    player = User()
    login_menu = LoginMenu(player)
    clock = pygame.time.Clock()

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        if player.get_login_time() is None:
            login_menu.update(events)
            login_menu.draw(surface)

        pygame.display.update()

        clock.tick(60)


if __name__ == "__main__":
    main()
