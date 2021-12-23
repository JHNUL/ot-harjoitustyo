import unittest
from datetime import datetime
from db_connection import get_db_connection
from models.player import Player
from models.score import Score
from repositories.player_repository import PlayerRepository
from services.player_service import PlayerService


class TestPlayerService(unittest.TestCase):
    def setUp(self):
        self.connection = get_db_connection()
        self.player_repository = PlayerRepository(self.connection)
        self.player_service = PlayerService(self.player_repository)

    def clear_db(self):
        self.connection.cursor().execute("DELETE FROM Players;")
        self.connection.commit()

    def test_player_login_creates_new_player(self):
        count = self.connection.cursor().execute("SELECT count(*) FROM Players;")
        count = count.fetchone()
        self.assertEqual(count[0], 0)
        res = self.player_service.player_login(name="Blinky")
        self.assertIsInstance(res, Player)
        count = self.connection.cursor().execute("SELECT count(*) FROM Players;")
        count = count.fetchone()
        self.assertEqual(count[0], 1)
        self.clear_db()

    def test_player_login_does_not_create_duplicates(self):
        count = self.connection.cursor().execute("SELECT count(*) FROM Players;")
        count = count.fetchone()
        self.assertEqual(count[0], 0)
        self.player_service.player_login(name="Blinky")
        count = self.connection.cursor().execute("SELECT count(*) FROM Players;")
        count = count.fetchone()
        self.assertEqual(count[0], 1)
        self.player_service.player_login(name="Blinky")
        count = self.connection.cursor().execute("SELECT count(*) FROM Players;")
        count = count.fetchone()
        self.assertEqual(count[0], 1)
        self.clear_db()

    def test_player_updates_login_time_for_existing_player(self):
        res = self.player_service.player_login(name="Blinky")
        original_login = res.last_login
        res = self.player_service.player_login(name="Blinky")
        self.assertLess(original_login, res.last_login)
        self.clear_db()
