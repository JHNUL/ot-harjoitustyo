import pygame
from game.sprites.enemy import Enemy
from game.sprites.nugget import Nugget
from game.sprites.pac import Pac
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
        self._sprites = pygame.sprite.Group()
        self._walls = pygame.sprite.Group()
        self._nuggets = pygame.sprite.Group()
        self._enemies = pygame.sprite.Group()
        self._score_service = score_service
        self.is_finished = False
        self.pac = None
        self.current_score = score
        self.top_scores = self._get_top_scores()
        self._create_level()

    def _get_top_scores(self) -> str:
        """Get the top scores

        Returns:
            str: string with the top scores and players
        """
        scores = self._score_service.get_top_scores_with_player_names(3)
        leaders = ", ".join(
            [f"{i+1}: {s[1]} {s[0]}" for i, s in enumerate(scores)])
        return leaders

    def _create_level(self):
        """Create the level from level map"""
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

        self._sprites.add(self.pac, self._walls, self._nuggets, self._enemies)

    def _check_collision(self, sprites: pygame.sprite.Group, do_kill=False) -> int:
        """Check collisions between Pac and other sprites

        Args:
            sprites (pygame.sprite.Group): collection of sprites to check against
            do_kill (bool, optional): if True, remove from collection. Defaults to False.

        Returns:
            int: number over 0 if there is collision
        """
        return len(pygame.sprite.spritecollide(self.pac, sprites, do_kill))

    def _check_collisions(self):
        """Check collisions between several groups of sprites and Pac
        and handle score and lives accordingly.
        """
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

    def _move_enemies(self):
        """Calls move method from every enemy and checks collisions"""
        for enemy in self._enemies:
            enemy.move(self._walls)
            self._check_collisions()

    def reset(self):
        """Reset the level. Kills Pac and enemies, resets score."""
        if self.pac is not None:
            self.pac.kill()
        for enemy in self._enemies:
            enemy.kill()
        self.current_score.reset()
        self.top_scores = self._get_top_scores()
        self._create_level()
        self.is_finished = False

    def do_update(self, move_enemies=False, direction=None):
        """Moves enemies and Pac.

        Args:
            move_enemies (bool, optional): if True moves enemies. Defaults to False.
            direction (Direction, optional): direction for Pac. Defaults to None.
        """
        if self.is_finished:
            return
        if move_enemies:
            self._move_enemies()
        if direction:
            self.pac.move(direction, self._walls)
        self._check_collisions()
        if self.pac.ephemeral:
            self.pac.count_down()

    def draw(self, surface: pygame.Surface):
        """Draws the sprites on the game surface

        Args:
            surface (pygame.Surface): Surface to draw on
        """
        self._sprites.draw(surface)
