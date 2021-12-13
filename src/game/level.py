import pygame
from game.sprites.enemy import Enemy
from game.sprites.nugget import Nugget
from game.sprites.pac import Pac
from game.sprites.wall import Wall
from models.score import Score
from services.score_service import ScoreService
from utils import normalize


class Level:
    def __init__(self, level_map, score: Score, score_service: ScoreService):
        self.is_finished = False
        self.pac = None
        self._map = level_map
        self.sprites = pygame.sprite.Group()
        self._walls = pygame.sprite.Group()
        self._nuggets = pygame.sprite.Group()
        self._enemies = pygame.sprite.Group()
        self._score_service = score_service
        self.current_score = score
        self.top_scores = self._get_top_scores()
        self._create_level()


    def _get_top_scores(self):
        scores = self._score_service.get_scores_with_player_names(3)
        leaders = ", ".join([f"{i+1}: {s[1]} {s[0]}" for i, s in enumerate(scores)])
        return leaders

    def _create_level(self):
        for y in range(len(self._map)):
            for x in range(len(self._map[0])):
                cell = self._map[y][x]
                if cell == 0:
                    self._nuggets.add(Nugget(normalize(x), normalize(y)))
                elif cell == 1:
                    self._walls.add(Wall(normalize(x), normalize(y)))
                elif cell == 2:
                    self.pac = Pac(normalize(x), normalize(y))
                elif cell == 3:
                    self._enemies.add(Enemy(normalize(x), normalize(y)))

        self.sprites.add(self.pac, self._walls, self._nuggets, self._enemies)

    def _check_collision(self, sprites, do_kill=False):
        return len(pygame.sprite.spritecollide(self.pac, sprites, do_kill))

    def _increase_score(self):
        self.current_score.increase()

    def _check_collisions(self):
        if self.pac.ephemeral:
            return
        if self._check_collision(self._nuggets, True):
            self.current_score.increase()
            if len(self._nuggets) == 0:
                self.is_finished = True
                self._score_service.add_score(self.current_score)

        if self._check_collision(self._enemies):
            self.pac.lives -= 1
            self.pac.ephemeral = True
            if self.pac.lives == 0:
                self.is_finished = True

    def reset(self):
        if self.pac is not None:
            self.pac.kill()
        for enemy in self._enemies:
            enemy.kill()
        self.current_score.reset()
        self._get_top_scores()
        self._create_level()
        self.is_finished = False

    def _move_enemies(self):
        for enemy in self._enemies:
            enemy.move(self._walls)
            self._check_collisions()

    def do_update(self, move_enemies=False, direction=None):
        if self.is_finished:
            return
        if move_enemies:
            self._move_enemies()
        if direction:
            self.pac.move(direction, self._walls)
        self._check_collisions()
        if self.pac.ephemeral:
            self.pac.count_down()
