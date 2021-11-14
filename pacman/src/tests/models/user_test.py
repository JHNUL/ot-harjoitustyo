import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    def test_initialize_user_without_arguments(self):
        user = User()
        self.assertEqual(user.username, None)
        self.assertEqual(user.playername, None)
        self.assertEqual(user.login_time, None)

    def test_initialize_user_with_arguments(self):
        user = User(username='mock', playername='user')
        self.assertEqual(user.username, 'mock')
        self.assertEqual(user.playername, 'user')
        self.assertEqual(user.login_time, None)

    def test_set_login_time(self):
        user = User()
        time = datetime.now().isoformat()
        user.set_login_time(time)
        self.assertEqual(user.login_time, time)
