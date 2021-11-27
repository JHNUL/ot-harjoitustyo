import pygame
from game.sprites.nugget import Nugget
from game.sprites.pac import Pac
from game.sprites.wall import Wall
from models.score import Score
from utils import normalize
from constants import CELL_SIZE


class Level:
    def __init__(self, level_map, score: Score):
        self.pac = None
        self.walls = pygame.sprite.Group()
        self.nuggets = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.current_score = score
        self._create_level(level_map)

    def _create_level(self, level_map):
        for y in range(len(level_map)):  # pylint: disable=consider-using-enumerate
            for x in range(len(level_map[0])):
                cell = level_map[y][x]
                if cell == 2:
                    self.pac = Pac(normalize(x), normalize(y))
                elif cell == 1:
                    self.walls.add(Wall(normalize(x), normalize(y)))
                elif cell == 0:
                    self.nuggets.add(Nugget(normalize(x), normalize(y)))

        self.sprites.add(self.pac, self.walls, self.nuggets)

    def _check_collision(self, sprites, do_kill=False):
        return len(pygame.sprite.spritecollide(self.pac, sprites, do_kill))

    def _increase_score(self):
        self.current_score.increase()

    def move_pac(self, direction):
        d_x, d_y = 0, 0
        if direction == pygame.K_LEFT:
            d_x, d_y = -CELL_SIZE, 0
        elif direction == pygame.K_RIGHT:
            d_x, d_y = CELL_SIZE, 0
        elif direction == pygame.K_UP:
            d_x, d_y = 0, -CELL_SIZE
        elif direction == pygame.K_DOWN:
            d_x, d_y = 0, CELL_SIZE

        if d_x or d_y:
            self.pac.rect.move_ip(d_x, d_y)

            if self._check_collision(self.walls):
                self.pac.rect.move_ip(-d_x, -d_y)

            if self._check_collision(self.nuggets, True):
                self.current_score.increase()
