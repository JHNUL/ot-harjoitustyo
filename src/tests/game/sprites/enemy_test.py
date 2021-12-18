import unittest

import pygame
from constants import Direction
from game.sprites.enemy import Enemy
from game.sprites.wall import Wall
from game.utils import normalize


class TestEnemy(unittest.TestCase):
    def setUp(self):
        self.walls = pygame.sprite.Group()
        self.walls.add(
            [Wall(normalize(1), normalize(1), 1), Wall(normalize(2), normalize(1), 1), Wall(normalize(3), normalize(1), 1)])

    def test_is_initialized_with_x_and_y_pos(self):
        enemy = Enemy(1, 2)
        self.assertEqual(enemy.rect.x, 1)
        self.assertEqual(enemy.rect.y, 2)

    def test_can_move(self):
        enemy = Enemy(normalize(1), normalize(2))
        self.assertEqual(enemy.rect.x, normalize(1))
        self.assertEqual(enemy.rect.y, normalize(2))
        enemy.move(self.walls, Direction.RIGHT)
        self.assertEqual(enemy.rect.x, normalize(2))
        self.assertEqual(enemy.rect.y, normalize(2))

    def test_cannot_move_through_walls(self):
        enemy = Enemy(normalize(1), normalize(2))
        self.assertEqual(enemy.rect.x, normalize(1))
        self.assertEqual(enemy.rect.y, normalize(2))
        enemy.move(self.walls, Direction.UP)
        self.assertEqual(enemy.rect.x, normalize(1))
        self.assertEqual(enemy.rect.y, normalize(2))

    def test_set_vulnerable(self):
        enemy = Enemy(1, 2)
        self.assertEqual(enemy.vulnerable, False)
        enemy.set_vulnerable()
        self.assertEqual(enemy.vulnerable, True)

    def test_count_down(self):
        enemy = Enemy(1, 2)
        self.assertEqual(enemy.timer, 60)
        enemy.set_vulnerable()
        for i in range(60):
            enemy.count_down()
            if i < 59:
                self.assertEqual(enemy.timer, 60-i-1)
                self.assertEqual(enemy.vulnerable, True)
            else:
                self.assertEqual(enemy.timer, 60)
                self.assertEqual(enemy.vulnerable, False)
