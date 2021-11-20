from sqlite3 import Connection
from models.player import Player


class PlayerRepository:
    def __init__(self, connection: 'Connection'):
        self._connection = connection

    def add_player(self, playername) -> bool:
        print('adding player', playername)
        self._connection.cursor().execute(
            "INSERT INTO Players(playername) VALUES (?);", (playername,))
        self._connection.commit()
        return True

    def find_player(self, playername) -> 'Player':
        cursor = self._connection.cursor().execute(
            "SELECT * FROM Players WHERE playername = (?);", (playername,))
        row = cursor.fetchone()
        if row is None:
            return None
        return Player(row['id'], row['playername'], row['last_login'])

    def set_last_login(self, playername, timestamp) -> bool:
        cursor = self._connection.cursor().execute(
            "SELECT * FROM Players WHERE playername = (?);", (playername,))
        row = cursor.fetchone()
        if row is None:
            return False
        cursor.execute("UPDATE Players SET last_login = (?) WHERE id = (?)",
                       (timestamp, row['id']))
        self._connection.commit()
        return True
