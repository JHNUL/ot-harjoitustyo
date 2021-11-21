import pygame
from game.sprites.nugget import Nugget
from game.sprites.pac import Pac
from game.sprites.wall import Wall
from utils import normalize
from constants import CELL_SIZE


class Level:
    def __init__(self, level_map):
        self.pac = None
        self.walls = pygame.sprite.Group()
        self.nuggets = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self._create_level(level_map)

    def _create_level(self, level_map):
        for y in range(len(level_map)):
            for x in range(len(level_map[0])):
                cell = level_map[y][x]
                if cell == 2:
                    self.pac = Pac(normalize(x), normalize(y))
                elif cell == 1:
                    self.walls.add(Wall(normalize(x), normalize(y)))
                elif cell == 0:
                    self.nuggets.add(Nugget(normalize(x), normalize(y)))

        self.sprites.add(self.pac, self.walls, self.nuggets)

    def move_pac(self, direction):
        if direction == pygame.K_LEFT:
            self.pac.rect.move_ip(-CELL_SIZE, 0)
        elif direction == pygame.K_RIGHT:
            self.pac.rect.move_ip(CELL_SIZE, 0)
        elif direction == pygame.K_UP:
            self.pac.rect.move_ip(0, -CELL_SIZE)
        elif direction == pygame.K_DOWN:
            self.pac.rect.move_ip(0, CELL_SIZE)
