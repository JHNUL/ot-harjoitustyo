from datetime import datetime
from models.score import Score
from repositories.score_repository import ScoreRepository


class ScoreService:
    """Score service class, layer between logic/ui modules and repository class"""

    def __init__(self, score_repository: ScoreRepository):
        """Constructor

        Args:
            score_repository (ScoreRepository): score repository
        """
        self._score_repository = score_repository

    def add_score(self, score: Score) -> bool:
        """Add new score

        Args:
            score (Score): score object

        Returns:
            bool: True if success
        """
        score.set_timestamp(datetime.now().timestamp())
        self._score_repository.add_score(score)

    def get_top_scores_with_player_names(self, count: int) -> list:
        """Find top scores with the names of the players who made them

        Args:
            count (int): amount of results to limit

        Returns:
            list: triplets of score value, player name and score timestamp
        """
        return self._score_repository.find_top_scores_with_player_names(count)
