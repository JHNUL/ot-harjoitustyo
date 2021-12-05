from sqlite3 import Connection
from models.player import Player


class PlayerRepository:
    def __init__(self, connection: Connection):
        self._connection = connection

    def add_player(self, player: Player) -> Player:
        cursor = self._connection.cursor().execute(
            "INSERT INTO Players(name, last_login) VALUES (?,?);", (player.name, player.last_login))
        self._connection.commit()
        player_id = cursor.lastrowid
        cursor = self._connection.cursor().execute(
            f"SELECT * FROM Players WHERE id = {player_id};")
        row = cursor.fetchone()
        if row is None:
            return None
        return Player(row['id'], row['name'], row['last_login'])

    def find_player_by_name(self, name) -> Player:
        cursor = self._connection.cursor().execute(
            "SELECT * FROM Players WHERE name = (?);", (name,))
        row = cursor.fetchone()
        if row is None:
            return None
        return Player(row['id'], row['name'], row['last_login'])

    def update_player(self, player: Player) -> bool:
        self._connection.cursor().execute(
            "UPDATE Players SET name = (?), last_login = (?) WHERE id = (?)",
            (player.name, player.last_login, player.id))
        self._connection.commit()
        return True
