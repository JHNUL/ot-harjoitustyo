import pygame
from game.sprites.enemy import Enemy
from game.sprites.nugget import Nugget
from game.sprites.pac import Pac
from game.sprites.super_nugget import SuperNugget
from game.sprites.wall import Wall
from game.utils import normalize
from models.score import Score
from services.score_service import ScoreService


class Level:
    """Class containing the logic for level

    Attributes:
        is_finished (bool): flag to indicate if level is finished
        pac (Pac): Pac object
        current_score (Score): current score
        top_scores (str): top scores from when the game started
    """

    def __init__(self, level_map: list, score: Score, score_service: ScoreService):
        """Constructor

        Args:
            level_map (list): list of lists representing the level labyrinth
            score (Score): score object
            score_service (ScoreService): score service object
        """
        self._map = level_map
        self._score_service = score_service
        self.is_finished = False
        self.current_score = score
        self.top_scores = self._get_top_scores()
        self._create_level()

    def _get_top_scores(self) -> str:
        scores = self._score_service.get_top_scores_with_player_names(3)
        if scores is not None:
            leaders = ", ".join(
                [f"{i+1}: {s[1]} {s[0]}" for i, s in enumerate(scores)])
            return leaders
        return "Error fetching leaderboard"

    def _create_level(self):
        self._sprites = pygame.sprite.Group()
        self._sprites = pygame.sprite.Group()
        self._walls = pygame.sprite.Group()
        self._nuggets = pygame.sprite.Group()
        self._super_nuggets = pygame.sprite.Group()
        self._enemies = pygame.sprite.Group()
        self.pac = None
        for y in range(len(self._map)):
            for x in range(len(self._map[0])):
                cell = self._map[y][x]
                if cell == 0:
                    self._nuggets.add(Nugget(normalize(x), normalize(y)))
                elif cell in [1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
                    self._walls.add(Wall(normalize(x), normalize(y), cell))
                elif cell == 2:
                    self.pac = Pac(normalize(x), normalize(y))
                elif cell == 3:
                    self._enemies.add(Enemy(normalize(x), normalize(y)))
                elif cell == 4:
                    self._super_nuggets.add(
                        SuperNugget(normalize(x), normalize(y)))

        self._sprites.add(
            self._walls,
            self._nuggets,
            self._super_nuggets,
            self._enemies,
            self.pac
        )

    def _check_collision(self, sprites: pygame.sprite.Group, do_kill=False) -> int:
        return len(pygame.sprite.spritecollide(self.pac, sprites, do_kill))

    def _check_collisions(self):
        if self.pac.ephemeral:
            return
        if self._check_collision(self._nuggets, do_kill=True):
            self.current_score.increase()
            if len(self._nuggets) == 0:
                self.is_finished = True
                score_id = self._score_service.add_score(self.current_score)
                if score_id is not None:
                    self.current_score.set_id(score_id)

        if self._check_collision(self._super_nuggets, do_kill=True):
            for enemy in self._enemies:
                enemy.set_vulnerable()

        for enemy in self._enemies:
            if enemy.vulnerable and pygame.sprite.collide_rect(self.pac, enemy):
                enemy.kill()
                self.current_score.increase(10)
            elif pygame.sprite.collide_rect(self.pac, enemy):
                if not self.pac.ephemeral:
                    self.pac.lives -= 1
                    self.pac.set_ephemeral()
                if self.pac.lives == 0:
                    self.is_finished = True
                    break

    def _move_enemies(self, move_vulnerable=False):
        for enemy in self._enemies:
            if enemy.vulnerable and move_vulnerable:
                enemy.move(self._walls)
                enemy.count_down()
            elif not enemy.vulnerable and not move_vulnerable:
                enemy.move(self._walls)
            self._check_collisions()

    def reset(self):
        """Reset the level including score."""
        self.current_score.reset()
        self.top_scores = self._get_top_scores()
        self._create_level()
        self.is_finished = False

    def do_update(
        self,
        move_enemies=False,
        move_vulnerable_enemies=False,
        direction=None,
        change_pac_mouth=False
    ):
        """Moves enemies and Pac.

        Args:
            move_enemies (bool, optional): if True moves enemies. Defaults to False.
            move_vulnerable_enemies (bool, optional): if True moves enemies who
            are in vulnerable state. Defaults to False.
            direction (Direction, optional): direction for Pac. Defaults to None.
            change_pac_mouth (bool, optional): pac mouth position should change. Defaults to False.
        """
        if move_enemies:
            self._move_enemies()
        if move_vulnerable_enemies:
            self._move_enemies(move_vulnerable=True)
        if direction:
            self.pac.move(direction, self._walls)
        self._check_collisions()
        if self.pac.ephemeral:
            self.pac.count_down()
        if change_pac_mouth:
            self.pac.change_mouth()

    def draw(self, surface: pygame.Surface):
        """Draws the sprites on the game surface

        Args:
            surface (pygame.Surface): Surface to draw on
        """
        self._sprites.draw(surface)
