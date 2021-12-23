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

    def add_score(self, score: Score) -> int:
        """Add new score

        Args:
            score (Score): score object

        Returns:
            int: id of the inserted Score or None if insertion failed
        """
        score.set_timestamp(datetime.now().timestamp())
        try:
            score_id = self._score_repository.add_score(score)
            return score_id
        except Exception:
            return None

    def get_top_scores_with_player_names(self, count: int) -> list:
        """Find top scores with the names of the players who made them

        Args:
            count (int): amount of results to limit

        Returns:
            list: triplets of score value, player name and score timestamp
            or None in case of error.
        """
        try:
            tops = self._score_repository.find_top_scores_with_player_names(count)
            return tops
        except Exception:
            return None

    def get_rank_of_score_by_id(self, score_id: int) -> int:
        """Find the ranking of a particular score

        Args:
            score_id (int): score id

        Returns:
            int: rank number or None if error.
        """
        try:
            all_scores = self._score_repository.find_all_scores()
            for i, score in enumerate(all_scores):
                if score_id == score.id:
                    return i+1
            return None # if score_id not in saved scores it's also error-worthy
        except Exception:
            return None
