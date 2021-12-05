import unittest
from datetime import datetime
from repositories.player_repository import PlayerRepository
from models.player import Player
from db_connection import get_db_connection


class TestPlayerRepository(unittest.TestCase):
    def setUp(self):
        self.connection = get_db_connection()
        self.test_player = Player(name="test_player")

    def clear_db(self):
        self.connection.cursor().execute("DELETE FROM Players;")
        self.connection.cursor().execute("DELETE FROM Scores;")
        self.connection.commit()

    def test_add_player_returns_player_when_no_error(self):
        repo = PlayerRepository(self.connection)
        res = repo.add_player(self.test_player)
        self.assertIsInstance(res, Player)
        self.clear_db()

    def test_add_player_adds_one_player_to_db(self):
        repo = PlayerRepository(self.connection)
        repo.add_player(self.test_player)
        cursor = self.connection.cursor().execute("SELECT COUNT(*) FROM Players;")
        res = cursor.fetchone()
        self.assertEqual(res[0], 1)
        self.clear_db()

    def test_find_player_returns_player(self):
        repo = PlayerRepository(self.connection)
        repo.add_player(self.test_player)
        player = repo.find_player_by_name("test_player")
        self.assertIsInstance(player, Player)
        self.clear_db()

    def test_returned_player_has_correct_instance_properties(self):
        repo = PlayerRepository(self.connection)
        repo.add_player(self.test_player)
        player = repo.find_player_by_name("test_player")
        self.assertEqual(player.id, 1)
        self.assertEqual(player.name, "test_player")
        self.assertEqual(player.last_login, None)
        self.clear_db()

    def test_find_player_returns_none_when_not_found(self):
        repo = PlayerRepository(self.connection)
        repo.add_player(self.test_player)
        player = repo.find_player_by_name("foo_bar")
        self.assertEqual(player, None)
        self.clear_db()

    def test_update_player_returns_true(self):
        repo = PlayerRepository(self.connection)
        repo.add_player(self.test_player)
        self.test_player.set_login_time(datetime.now().timestamp())
        res = repo.update_player(self.test_player)
        self.assertTrue(res)
        self.clear_db()
