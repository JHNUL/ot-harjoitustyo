import unittest

import pygame
from constants import MOVEMENTS
from game.sprites.pac import Pac
from game.sprites.wall import Wall
from game.utils import normalize


class TestPac(unittest.TestCase):
    def setUp(self):
        self.walls = pygame.sprite.Group()
        self.walls.add(
            [Wall(normalize(1), normalize(1)), Wall(normalize(2), normalize(1)), Wall(normalize(3), normalize(1))])

    def test_is_initialized_with_x_and_y_pos(self):
        pac = Pac(2, 2)
        self.assertEqual(pac.rect.x, 2)
        self.assertEqual(pac.rect.y, 2)

    def test_can_move(self):
        pac = Pac(normalize(3), normalize(2))
        self.assertEqual(pac.rect.x, normalize(3))
        self.assertEqual(pac.rect.y, normalize(2))
        pac.move(delta_coordinates=MOVEMENTS[pygame.K_DOWN], walls=self.walls)
        self.assertEqual(pac.rect.x, normalize(3))
        self.assertEqual(pac.rect.y, normalize(3))

    def test_cannot_move_through_walls(self):
        pac = Pac(normalize(3), normalize(2))
        self.assertEqual(pac.rect.x, normalize(3))
        self.assertEqual(pac.rect.y, normalize(2))
        pac.move(delta_coordinates=MOVEMENTS[pygame.K_UP], walls=self.walls)
        self.assertEqual(pac.rect.x, normalize(3))
        self.assertEqual(pac.rect.y, normalize(2))

    def test_count_down_to_zero_resets_timer(self):
        pac = Pac(2, 2)
        self.assertEqual(pac.timer, 20)
        for i in range(20):
            pac.count_down()
            if i < 19:
                self.assertEqual(pac.timer, 20-i-1)
            else:
                self.assertEqual(pac.timer, 20)

    def test_count_down_to_zero_sets_ephemeral_to_false(self):
        pac = Pac(2, 2)
        self.assertEqual(pac.timer, 20)
        pac.ephemeral = True
        for i in range(20):
            pac.count_down()
            if i < 19:
                self.assertEqual(pac.timer, 20-i-1)
                self.assertEqual(pac.ephemeral, True)
            else:
                self.assertEqual(pac.timer, 20)
                self.assertEqual(pac.ephemeral, False)

    def test_count_down_to_zero_flashes_damage_image(self):
        pac = Pac(2, 2)
        self.assertEqual(pac.timer, 20)
        pac.ephemeral = True
        for i in range(20):
            pac.count_down()
            if i < 19:
                if pac.timer % 2 == 0:
                    self.assertEqual(pac.image, pac.damage_image)
                else:
                    self.assertNotEqual(pac.image, pac.damage_image)
