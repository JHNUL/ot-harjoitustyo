from models.user import User
from datetime import datetime


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_user(self, username):
        return User(1, 'mock', 'user', datetime.now().isoformat())

    def create_user(self, username, playername):
        print(username, playername)
