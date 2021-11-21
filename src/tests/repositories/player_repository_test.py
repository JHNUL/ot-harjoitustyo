import unittest
from datetime import datetime
from repositories.player_repository import PlayerRepository
from models.player import Player
from db_connection import get_db_connection


class TestPlayerRepository(unittest.TestCase):
    def setUp(self):
        self.connection = get_db_connection()
        self.test_player = Player(playername="test_player")

    def clear_db(self):
        self.connection.cursor().execute("DELETE FROM Players;")
        self.connection.cursor().execute("DELETE FROM Scores;")
        self.connection.commit()

    def test_add_player_returns_true_when_no_error(self):
        repo = PlayerRepository(self.connection)
        res = repo.add_player(self.test_player)
        self.assertTrue(res)
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
        self.assertEqual(player.playername, "test_player")
        self.assertEqual(player.last_login, None)
        self.clear_db()

    def test_find_player_returns_none_when_not_found(self):
        repo = PlayerRepository(self.connection)
        repo.add_player(self.test_player)
        player = repo.find_player_by_name("foo_bar")
        self.assertEqual(player, None)
        self.clear_db()

    def test_set_last_login_returns_true(self):
        repo = PlayerRepository(self.connection)
        repo.add_player(self.test_player)
        self.test_player.set_login_time(datetime.now().timestamp())
        res = repo.set_last_login(self.test_player)
        self.assertTrue(res)
        self.clear_db()

    def test_set_last_login_returns_false_when_no_player_found(self):
        repo = PlayerRepository(self.connection)
        repo.add_player(self.test_player)
        not_added = Player("new_player")
        not_added.set_login_time(datetime.now().timestamp())
        res = repo.set_last_login(not_added)
        self.assertFalse(res)
        self.clear_db()

    def test_set_last_login_sets_timestamp(self):
        repo = PlayerRepository(self.connection)
        repo.add_player(self.test_player)
        cursor = self.connection.cursor().execute(
            "SELECT last_login FROM Players WHERE playername = 'test_player';")
        res = cursor.fetchone()
        self.assertIsNone(res[0])
        self.test_player.set_login_time(datetime.now().timestamp())
        repo.set_last_login(self.test_player)
        cursor = self.connection.cursor().execute(
            "SELECT last_login FROM Players WHERE playername = 'test_player';")
        res = cursor.fetchone()
        self.assertIsInstance(res[0], float)
        self.clear_db()
