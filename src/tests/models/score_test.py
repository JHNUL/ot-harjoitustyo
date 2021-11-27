import unittest
from models.score import Score


class TestScore(unittest.TestCase):
    def test_initialize_score(self):
        score = Score(100, player_id=1, score_timestamp=123.123)
        self.assertEqual(score.player_id, 1)
        self.assertEqual(score.score, 100)
        self.assertEqual(score.score_timestamp, 123.123)
