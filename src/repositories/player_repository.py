from sqlite3 import Connection
from models.player import Player


class PlayerRepository:
    def __init__(self, connection: Connection):
        self._connection = connection

    def add_player(self, player: Player) -> bool:
        self._connection.cursor().execute(
            "INSERT INTO Players(playername) VALUES (?);", (player.playername,))
        self._connection.commit()
        return True

    def find_player_by_name(self, playername) -> Player:
        cursor = self._connection.cursor().execute(
            "SELECT * FROM Players WHERE playername = (?);", (playername,))
        row = cursor.fetchone()
        if row is None:
            return None
        return Player(row['id'], row['playername'], row['last_login'])

    def set_last_login(self, player: Player) -> bool:
        cursor = self._connection.cursor().execute(
            "SELECT * FROM Players WHERE playername = (?);", (player.playername,))
        row = cursor.fetchone()
        if row is None:
            return False
        cursor.execute("UPDATE Players SET last_login = (?) WHERE id = (?)",
                       (player.last_login, row['id']))
        self._connection.commit()
        return True
