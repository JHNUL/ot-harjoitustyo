import pygame
from game.sprites.enemy import Enemy
from game.sprites.nugget import Nugget
from game.sprites.pac import Pac
from game.sprites.wall import Wall
from models.score import Score
from utils import normalize
from constants import CELL_SIZE


class Level:
    def __init__(self, level_map, score: Score):
        self.map = level_map
        self.pac = None
        self.walls = pygame.sprite.Group()
        self.nuggets = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.current_score = score
        self.is_finished = False
        self._create_level()

    def _create_level(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                cell = self.map[y][x]
                if cell == 0:
                    self.nuggets.add(Nugget(normalize(x), normalize(y)))
                elif cell == 1:
                    self.walls.add(Wall(normalize(x), normalize(y)))
                elif cell == 2:
                    self.pac = Pac(normalize(x), normalize(y))
                elif cell == 3:
                    self.enemies.add(Enemy(normalize(x), normalize(y)))

        self.sprites.add(self.pac, self.walls, self.nuggets, self.enemies)

    def reset(self):
        self.is_finished = False
        if self.pac is not None:
            self.pac.kill()
        self.current_score.reset()
        self._create_level()

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
                if len(self.nuggets) == 0:
                    self.is_finished = True

            if self._check_collision(self.enemies):
                self.pac.lives -= 1
                if self.pac.lives == 0:
                    self.is_finished = True
