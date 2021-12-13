from sqlite3 import Connection
from models.score import Score


class ScoreRepository:
    """Class that handles the persistence for Player objects"""

    def __init__(self, connection: Connection):
        """Constructor

        Args:
            connection (Connection): database connection
        """
        self._connection = connection

    def add_score(self, score: Score) -> bool:
        """Add new score

        Args:
            score (Score): score object

        Returns:
            bool: True if succeeded
        """
        self._connection.cursor().execute(
            "INSERT INTO Scores(player_id, timestamp, value) VALUES (?,?,?);",
            (score.player_id, score.timestamp, score.value)
        )
        self._connection.commit()
        return True

    def find_scores_by_player_id(self, player_id: int, limit=0) -> list:
        """Find scores with player id

        Args:
            player_id (int): player id
            limit (int, optional): limit the results. Defaults to 0.

        Returns:
            list: Score objects
        """
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


    def find_top_scores_with_player_names(self, limit=5) -> list:
        """Find top scores with the names of the players who made them

        Args:
            limit (int, optional): amount of results to limit. Defaults to 5.

        Returns:
            list: triplets of score value, player name and score timestamp
        """
        cursor = self._connection.cursor().execute(
            "SELECT value, name, timestamp FROM Scores LEFT JOIN Players ON Players.id = Scores.player_id ORDER BY Scores.value DESC LIMIT (?);", (limit,))
        rows = cursor.fetchall()
        if rows is None:
            return []
        return [(row['value'], row['name'], row['timestamp']) for row in rows]
