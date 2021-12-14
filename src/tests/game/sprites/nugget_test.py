import unittest

from game.sprites.nugget import Nugget


class TestNugget(unittest.TestCase):
    def test_is_initialized_with_x_and_y_pos(self):
        nugget = Nugget(2, 2)
        self.assertEqual(nugget.rect.x, 2)
        self.assertEqual(nugget.rect.y, 2)
