import unittest
from datetime import datetime
from models.player import Player


class TestUser(unittest.TestCase):
    def test_initialize_player_without_arguments(self):
        user = Player()
        self.assertEqual(user.playername, None)
        self.assertEqual(user.screenname, None)
        self.assertEqual(user.login_time, None)

    def test_initialize_player_with_arguments(self):
        user = Player(playername='mock')
        self.assertEqual(user.playername, 'mock')
        self.assertEqual(user.login_time, None)

    def test_set_login_time(self):
        user = Player()
        time = datetime.now().isoformat()
        user.set_login_time(time)
        self.assertEqual(user.login_time, time)
