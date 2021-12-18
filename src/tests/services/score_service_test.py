import unittest
from datetime import datetime
from db_connection import get_db_connection
from models.score import Score
from repositories.score_repository import ScoreRepository
from services.score_service import ScoreService


class TestScoreService(unittest.TestCase):
    def setUp(self):
        self.connection = get_db_connection()
        self.score_repository = ScoreRepository(self.connection)
        self.score_service = ScoreService(self.score_repository)

    def clear_db(self):
        self.connection.cursor().execute("DELETE FROM Scores;")
        self.connection.cursor().execute("DELETE FROM Players;")
        self.connection.commit()

    def add_player(self, name, last_login):
        self.connection.cursor().execute(
            "INSERT INTO Players(name, last_login) VALUES (?,?);", (name, last_login))

    def test_add_score_returns_id(self):
        score_id = self.score_service.add_score(
            Score(value=100, player_id=1, timestamp=123.23))
        score_id_2 = self.score_service.add_score(
            Score(value=100, player_id=1, timestamp=123.23))
        self.assertEqual(score_id, 1)
        self.assertEqual(score_id_2, 2)
        self.clear_db()

    def test_get_top_scores_with_player_names(self):
        self.add_player('foo', datetime.now().timestamp())
        self.add_player('faa', datetime.now().timestamp())
        self.score_service.add_score(
            Score(value=100, player_id=1, timestamp=123.23))
        self.score_service.add_score(
            Score(value=1220, player_id=2, timestamp=123.23))
        res = self.score_service.get_top_scores_with_player_names(10)
        self.assertEqual(res[0][0], 1220)
        self.assertEqual(res[0][1], 'faa')
        self.assertEqual(res[1][0], 100)
        self.assertEqual(res[1][1], 'foo')
        self.clear_db()

    def test_get_rank_of_score_by_id(self):
        self.score_service.add_score(
            Score(value=100, player_id=1, timestamp=123.23))
        self.score_service.add_score(
            Score(value=1220, player_id=2, timestamp=123.23))
        sid = self.score_service.add_score(
            Score(value=10, player_id=2, timestamp=123.23))
        sid2 = self.score_service.add_score(
            Score(value=1620, player_id=2, timestamp=123.23))
        res = self.score_service.get_rank_of_score_by_id(sid)
        res2 = self.score_service.get_rank_of_score_by_id(sid2)
        self.assertEqual(res, 4)
        self.assertEqual(res2, 1)
        self.clear_db()
