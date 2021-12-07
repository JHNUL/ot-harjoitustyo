from datetime import datetime
from models.score import Score
from repositories.score_repository import ScoreRepository


class ScoreService:
    def __init__(self, score_repository: ScoreRepository):
        self._score_repository = score_repository

    def add_score(self, score: Score) -> Score:
        score.set_timestamp(datetime.now().timestamp())
        self._score_repository.add_score(score)
        