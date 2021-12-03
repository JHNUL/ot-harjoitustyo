import unittest
from models.score import Score


class TestScore(unittest.TestCase):
    def test_initialize_score(self):
        score = Score(100, player_id=1, timestamp=123.123)
        self.assertEqual(score.player_id, 1)
        self.assertEqual(score.value, 100)
        self.assertEqual(score.timestamp, 123.123)

    def test_increase_score_default_amount(self):
        score = Score(100, player_id=1, timestamp=123.123)
        self.assertEqual(score.value, 100)
        score.increase()
        self.assertEqual(score.value, 101)

    def test_increase_score_custom_amount(self):
        score = Score(100, player_id=1, timestamp=123.123)
        self.assertEqual(score.value, 100)
        score.increase(20)
        self.assertEqual(score.value, 120)
