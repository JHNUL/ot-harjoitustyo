from sqlite3 import Connection
from models.score import Score


class ScoreRepository:
    def __init__(self, connection: Connection):
        self._connection = connection

    def add_score(self, score: Score) -> bool:
        self._connection.cursor().execute(
            "INSERT INTO Scores(player_id, timestamp, value) VALUES (?,?,?);",
            (score.player_id, score.timestamp, score.value)
        )
        self._connection.commit()
        return True

    def find_scores_by_player_id(self, player_id: int, limit=0) -> list:
        query = "SELECT * FROM Scores WHERE player_id = (?) ORDER BY value DESC;"
        params = (player_id,)
        if limit:
            query = "SELECT * FROM Scores WHERE player_id = (?) ORDER BY value DESC LIMIT (?);"
            params = (player_id, limit)
        cursor = self._connection.cursor().execute(query, params)
        rows = cursor.fetchall()
        if rows is None:
            return []
        return [Score(s['value'], s['player_id'], s['timestamp'], id_=s['id']) for s in rows]

    def find_top_scores(self, limit=5) -> list:
        cursor = self._connection.cursor().execute(
            "SELECT * FROM Scores ORDER BY value DESC LIMIT (?);", (limit,))
        rows = cursor.fetchall()
        if rows is None:
            return []
        return [Score(s['value'], s['player_id'], s['timestamp'], id_=s['id']) for s in rows]
