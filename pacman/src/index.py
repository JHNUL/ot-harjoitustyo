import pygame
from constants import DISPLAY_HEIGHT, DISPLAY_WIDTH
from models.user import User
from ui.menus.login_menu import LoginMenu
from repositories.user_repository import UserRepository


def main():
    pygame.init()
    surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    player = User()
    user_repo = UserRepository('foo')
    login_menu = LoginMenu(player, user_repo)
    clock = pygame.time.Clock()

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        surface.fill((0, 0, 0))

        # loop this while player is not logged in
        if player.login_time is None:
            login_menu.update(events)
            login_menu.draw(surface)
            pygame.display.flip()
            continue

        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()
