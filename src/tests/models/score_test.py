import unittest
from models.score import Score


class TestScore(unittest.TestCase):
    def test_initialize_score_without_arguments(self):
        score = Score()
        self.assertEqual(score.player_id, None)
        self.assertEqual(score.score, 0)
        self.assertEqual(score.score_timestamp, None)
