import unittest

from game.sprites.super_nugget import SuperNugget


class TestSuperNugget(unittest.TestCase):
    def test_is_initialized_with_x_and_y_pos(self):
        super_nugget = SuperNugget(2, 2)
        self.assertEqual(super_nugget.rect.x, 2)
        self.assertEqual(super_nugget.rect.y, 2)
