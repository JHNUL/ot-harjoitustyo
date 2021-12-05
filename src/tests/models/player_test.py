import unittest
from datetime import datetime
from models.player import Player


class TestPlayer(unittest.TestCase):
    def test_initialize_player_without_arguments(self):
        player = Player()
        self.assertEqual(player.name, None)
        self.assertEqual(player.last_login, None)

    def test_initialize_player_with_arguments(self):
        player = Player(name='mock', id_=5, last_login=123.123)
        self.assertEqual(player.name, 'mock')
        self.assertEqual(player.id, 5)
        self.assertEqual(player.last_login, 123.123)

    def test_set_login_time(self):
        player = Player()
        time = datetime.now().isoformat()
        player.set_login_time(time)
        self.assertEqual(player.last_login, time)
