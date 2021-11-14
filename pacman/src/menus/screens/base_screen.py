from pygame_menu import Menu
import constants as c


class BaseScreen:
    def __init__(self, title):
        self.menu = Menu(title, c.DISPLAY_WIDTH/2, c.DISPLAY_HEIGHT/2)

    def update(self, events):
        self.menu.update(events)

    def draw(self, surface):
        self.menu.draw(surface)
