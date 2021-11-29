import unittest
import pygame
from game.level import Level
from models.score import Score
from utils import normalize


TEST_MAP = [[1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 2, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1]]


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.score = Score(0)
        self.level = Level(TEST_MAP, self.score)

    def test_pac_can_move_along_corridor(self):
        self.assertEqual(self.level.pac.rect.x, normalize(4))
        self.assertEqual(self.level.pac.rect.y, normalize(2))
        self.level.move_pac(pygame.K_LEFT)
        self.level.move_pac(pygame.K_UP)
        self.assertEqual(self.level.pac.rect.x, normalize(3))
        self.assertEqual(self.level.pac.rect.y, normalize(1))

    def test_pac_cannot_move_through_walls(self):
        self.assertEqual(self.level.pac.rect.x, normalize(4))
        self.assertEqual(self.level.pac.rect.y, normalize(2))
        self.level.move_pac(pygame.K_RIGHT)
        self.level.move_pac(pygame.K_RIGHT)
        self.assertEqual(self.level.pac.rect.x, normalize(4))
        self.assertEqual(self.level.pac.rect.y, normalize(2))

    def test_collecting_nuggets_increases_score(self):
        self.assertEqual(self.score.value, 0)
        self.level.move_pac(pygame.K_LEFT)
        self.level.move_pac(pygame.K_UP)
        self.assertEqual(self.score.value, 2)

    def test_nuggets_are_removed_from_group(self):
        self.assertEqual(len(self.level.nuggets), 15)
        self.level.move_pac(pygame.K_LEFT)
        self.level.move_pac(pygame.K_UP)
        self.assertEqual(len(self.level.nuggets), 13)
