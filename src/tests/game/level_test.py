import unittest
import pygame
from game.level import Level
from game.enums import Direction
from models.score import Score
from repositories.score_repository import ScoreRepository
from db_connection import get_db_connection
from services.score_service import ScoreService
from utils import normalize
from constants import MOVEMENTS


TEST_MAP = [[1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 2, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1]]


class TestLevelWithoutEnemy(unittest.TestCase):
    def setUp(self):
        self.score = Score(value=0, player_id=5)
        self.score_service = ScoreService(score_repository=ScoreRepository(get_db_connection()))
        self.level = Level(TEST_MAP, self.score, self.score_service)

    def _move_pac(self, direction, times=1):
        loops = 0
        while loops < times:
            self.level.do_update(direction=direction)
            loops += 1

    def test_pac_can_move_along_corridor(self):
        self.assertEqual(self.level.pac.rect.x, normalize(4))
        self.assertEqual(self.level.pac.rect.y, normalize(2))
        self._move_pac(MOVEMENTS[pygame.K_LEFT])
        self._move_pac(MOVEMENTS[pygame.K_UP])
        self.assertEqual(self.level.pac.rect.x, normalize(3))
        self.assertEqual(self.level.pac.rect.y, normalize(1))

    def test_pac_cannot_move_through_walls(self):
        self.assertEqual(self.level.pac.rect.x, normalize(4))
        self.assertEqual(self.level.pac.rect.y, normalize(2))
        self._move_pac(MOVEMENTS[pygame.K_RIGHT], 2)
        self.assertEqual(self.level.pac.rect.x, normalize(4))
        self.assertEqual(self.level.pac.rect.y, normalize(2))

    def test_collecting_nuggets_increases_score(self):
        self.assertEqual(self.score.value, 0)
        self._move_pac(MOVEMENTS[pygame.K_LEFT])
        self._move_pac(MOVEMENTS[pygame.K_UP])
        self.assertEqual(self.score.value, 2)

    def test_nuggets_are_removed_from_group(self):
        self.assertEqual(len(self.level._nuggets), 15)
        self._move_pac(MOVEMENTS[pygame.K_LEFT])
        self._move_pac(MOVEMENTS[pygame.K_UP])
        self.assertEqual(len(self.level._nuggets), 13)

    def test_level_is_finished_when_all_nuggets_are_collected(self):
        self.assertEqual(len(self.level._nuggets), 15)
        self.assertEqual(self.level.is_finished, False)
        self._move_pac(MOVEMENTS[pygame.K_LEFT], 2)
        self._move_pac(MOVEMENTS[pygame.K_DOWN])
        self._move_pac(MOVEMENTS[pygame.K_RIGHT], 2)
        self._move_pac(MOVEMENTS[pygame.K_DOWN])
        self._move_pac(MOVEMENTS[pygame.K_LEFT], 3)
        self._move_pac(MOVEMENTS[pygame.K_UP], 3)
        self._move_pac(MOVEMENTS[pygame.K_RIGHT], 3)
        self.assertEqual(len(self.level._nuggets), 0)
        self.assertEqual(self.level.is_finished, True)


TEST_MAP_WITH_ENEMY = [[1, 1, 1, 1, 1, 1],
                       [1, 3, 0, 2, 0, 1],
                       [1, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 1],
                       [1, 1, 1, 1, 1, 1]]


class TestLevelWithEnemy(unittest.TestCase):
    def setUp(self):
        self.score = Score(value=0)
        self.score_service = ScoreService(score_repository=ScoreRepository(get_db_connection()))
        self.level = Level(TEST_MAP_WITH_ENEMY, self.score, self.score_service)
        self.enemy = [x for x in self.level._enemies][0]

    def _move_pac(self, direction, times=1):
        loops = 0
        while loops < times:
            self.level.do_update(direction=direction)
            loops += 1

    def test_enemies_can_move(self):
        self.assertEqual(self.enemy.rect.x, normalize(1))
        self.assertEqual(self.enemy.rect.y, normalize(1))
        self.enemy.move(self.level._walls, Direction.RIGHT)
        self.enemy.move(self.level._walls, Direction.RIGHT)
        self.assertEqual(self.enemy.rect.x, normalize(3))
        self.assertEqual(self.enemy.rect.y, normalize(1))

    def test_enemies_cannot_move_through_walls(self):
        self.assertEqual(self.enemy.rect.x, normalize(1))
        self.assertEqual(self.enemy.rect.y, normalize(1))
        self.enemy.move(self.level._walls, Direction.RIGHT)
        self.enemy.move(self.level._walls, Direction.UP)
        self.enemy.move(self.level._walls, Direction.UP)
        self.assertEqual(self.enemy.rect.x, normalize(2))
        self.assertEqual(self.enemy.rect.y, normalize(1))

    def test_life_is_lost_when_pac_moves_into_enemy(self):
        self.assertEqual(self.level.pac.lives, 3)
        self._move_pac(MOVEMENTS[pygame.K_LEFT], 2)
        self.assertEqual(self.level.pac.lives, 2)

    def test_life_is_lost_when_enemy_moves_into_pac(self):
        self.assertEqual(self.level.pac.lives, 3)
        self.enemy.move(self.level._walls, Direction.RIGHT)
        self.enemy.move(self.level._walls, Direction.RIGHT)
        self.level.do_update()  # to check collisions
        self.assertEqual(self.level.pac.lives, 2)

    def test_pac_goes_into_ephemeral_mode_after_collision_with_lives_left(self):
        self.assertEqual(self.level.pac.ephemeral, False)
        self._move_pac(MOVEMENTS[pygame.K_LEFT], 2)
        self.assertEqual(self.level.pac.ephemeral, True)

    def test_timer_reduces_with_update_when_in_ephemeral_mode(self):
        self.level.pac.ephemeral = True
        self.assertEqual(self.level.pac.timer, 20)
        self.level.do_update()
        self.assertEqual(self.level.pac.timer, 19)

    def test_timer_does_not_reduce_with_update_when_not_in_ephemeral_mode(self):
        self.assertEqual(self.level.pac.ephemeral, False)
        self.assertEqual(self.level.pac.timer, 20)
        self.level.do_update()
        self.assertEqual(self.level.pac.timer, 20)

    def test_ephemeral_mode_turns_off_when_timer_is_zero_or_less(self):
        self.level.pac.ephemeral = True
        self.assertEqual(self.level.pac.timer, 20)
        for _i in range(20):
            self.level.do_update()
        self.assertEqual(self.level.pac.ephemeral, False)

    def test_timer_is_reset_when_value_is_zero_or_less(self):
        self.level.pac.ephemeral = True
        self.assertEqual(self.level.pac.timer, 20)
        self.level.do_update()
        self.assertEqual(self.level.pac.timer, 19)
        for _i in range(20):
            self.level.do_update()
        self.assertEqual(self.level.pac.timer, 20)

    def test_losing_last_life_ends_level(self):
        self.assertEqual(self.level.is_finished, False)
        self.assertEqual(self.level.pac.lives, 3)
        self._move_pac(MOVEMENTS[pygame.K_LEFT], 2)
        self.assertEqual(self.level.pac.lives, 2)
        for _i in range(20):
            self.level.do_update()
        self._move_pac(MOVEMENTS[pygame.K_DOWN])
        self._move_pac(MOVEMENTS[pygame.K_UP])
        self.assertEqual(self.level.pac.lives, 1)
        for _i in range(20):
            self.level.do_update()
        self._move_pac(MOVEMENTS[pygame.K_DOWN])
        self._move_pac(MOVEMENTS[pygame.K_UP])
        self.assertEqual(self.level.pac.lives, 0)
        self.assertEqual(self.level.is_finished, True)
