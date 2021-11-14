from models.score import Score


class ScoreRepository:
    def __init__(self, connection):
        self._connection = connection

    def list_scores(self, limit=5):
        return [Score(score=x) for x in range(limit)]
