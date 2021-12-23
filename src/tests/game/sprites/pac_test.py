import unittest

import pygame
from constants import DIRECTION_MAP
from game.sprites.pac import Pac
from game.sprites.wall import Wall
from game.utils import normalize


class TestPac(unittest.TestCase):
    def setUp(self):
        self.walls = pygame.sprite.Group()
        self.walls.add(
            [Wall(normalize(1), normalize(1), 1), Wall(normalize(2), normalize(1), 1), Wall(normalize(3), normalize(1), 1)])

    def test_is_initialized_with_x_and_y_pos(self):
        pac = Pac(2, 2)
        self.assertEqual(pac.rect.x, 2)
        self.assertEqual(pac.rect.y, 2)

    def test_can_move(self):
        pac = Pac(normalize(3), normalize(2))
        self.assertEqual(pac.rect.x, normalize(3))
        self.assertEqual(pac.rect.y, normalize(2))
        pac.move(direction=DIRECTION_MAP[pygame.K_DOWN], walls=self.walls)
        self.assertEqual(pac.rect.x, normalize(3))
        self.assertEqual(pac.rect.y, normalize(3))

    def test_cannot_move_through_walls(self):
        pac = Pac(normalize(3), normalize(2))
        self.assertEqual(pac.rect.x, normalize(3))
        self.assertEqual(pac.rect.y, normalize(2))
        pac.move(direction=DIRECTION_MAP[pygame.K_UP], walls=self.walls)
        self.assertEqual(pac.rect.x, normalize(3))
        self.assertEqual(pac.rect.y, normalize(2))
