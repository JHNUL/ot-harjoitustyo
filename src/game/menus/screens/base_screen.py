from pygame_menu import Menu


class BaseScreen:
    def __init__(self, title):
        self.menu = Menu(title, 500, 300)

    def update(self, events):
        self.menu.update(events)

    def draw(self, surface):
        self.menu.draw(surface)
