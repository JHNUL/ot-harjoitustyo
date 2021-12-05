from datetime import datetime
import pygame
from game.sprites.enemy import Enemy
from game.sprites.nugget import Nugget
from game.sprites.pac import Pac
from game.sprites.wall import Wall
from models.score import Score
from repositories.score_repository import ScoreRepository
from utils import normalize


class Level:
    def __init__(self, level_map, score: Score, score_repository: ScoreRepository):
        self.map = level_map
        self.pac = None
        self.walls = pygame.sprite.Group()
        self.nuggets = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.current_score = score
        self.is_finished = False
        self.score_repo = score_repository
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

    def _check_collision(self, sprites, do_kill=False):
        return len(pygame.sprite.spritecollide(self.pac, sprites, do_kill))

    def _increase_score(self):
        self.current_score.increase()

    def _check_collisions(self):
        if self.pac.ephemeral:
            return
        if self._check_collision(self.nuggets, True):
            self.current_score.increase()
            if len(self.nuggets) == 0:
                self.is_finished = True
                self.current_score.set_timestamp(datetime.now().timestamp())
                self.score_repo.add_score(self.current_score)

        if self._check_collision(self.enemies):
            self.pac.lives -= 1
            self.pac.ephemeral = True
            if self.pac.lives == 0:
                self.is_finished = True

    def reset(self):
        if self.pac is not None:
            self.pac.kill()
        for enemy in self.enemies:
            enemy.kill()
        self.current_score.reset()
        self._create_level()
        self.is_finished = False

    def move_enemies(self):
        if self.is_finished:
            return
        for enemy in self.enemies:
            enemy.move(self.walls)

    def do_update(self, direction=None, timedelta=0):
        if self.is_finished:
            return
        if direction:
            self.pac.move(direction, self.walls)
        self._check_collisions()
        if self.pac.ephemeral:
            self.pac.count_down(timedelta)
