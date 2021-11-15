from models.player import Player
from datetime import datetime


class PlayerRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_player(self, playername):
        return Player(1, 'mock', 'player', datetime.now().isoformat())

    def create_player(self, playername):
        pass
