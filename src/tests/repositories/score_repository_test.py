import unittest
from datetime import datetime
from models.score import Score
from repositories.score_repository import ScoreRepository
from db_connection import get_db_connection


class TestScoreRepository(unittest.TestCase):
    def setUp(self):
        self.connection = get_db_connection()
        self.test_score = Score(10, player_id=1, timestamp=1234.1234)

    def clear_db(self):
        self.connection.cursor().execute("DELETE FROM Players;")
        self.connection.cursor().execute("DELETE FROM Scores;")
        self.connection.commit()

    def test_add_score_returns_true_when_no_error(self):
        repo = ScoreRepository(self.connection)
        res = repo.add_score(self.test_score)
        self.assertTrue(res)
        self.clear_db()

    def test_find_score_by_player_id_returns_empty_list(self):
        repo = ScoreRepository(self.connection)
        repo.add_score(self.test_score)
        res = repo.find_scores_by_player_id(-99)
        self.assertIsInstance(res, list)
        self.assertTrue(len(res) == 0)
        self.clear_db()

    def test_find_score_by_player_id_returns_scores_for_player(self):
        repo = ScoreRepository(self.connection)
        for x in range(5):
            repo.add_score(Score(x+10, 1, datetime.now().timestamp()))
            repo.add_score(Score(x+20, 2, datetime.now().timestamp()))

        res = repo.find_scores_by_player_id(1)
        self.assertIsInstance(res, list)
        self.assertTrue(len(res) == 5)
        for score in res:
            self.assertIsInstance(score, Score)
        self.clear_db()

    def test_find_score_by_player_id_returns_scores_in_descending_order(self):
        repo = ScoreRepository(self.connection)
        for x in range(5):
            repo.add_score(Score(x+10, 1, datetime.now().timestamp()))

        res = repo.find_scores_by_player_id(1)
        for i in range(1, 5):
            self.assertTrue(res[i-1].value > res[i].value)
        self.clear_db()

    def test_find_score_by_player_id_returns_top_n_scores_for_player(self):
        repo = ScoreRepository(self.connection)
        for x in range(10):
            repo.add_score(Score(x+10, 1, datetime.now().timestamp()))

        res = repo.find_scores_by_player_id(1, 3)
        self.assertTrue(len(res) == 3)
        self.assertTrue(res[0].value == 19)
        self.assertTrue(res[1].value == 18)
        self.assertTrue(res[2].value == 17)
        self.clear_db()
