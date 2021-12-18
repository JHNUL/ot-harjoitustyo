from datetime import datetime
from models.player import Player
from repositories.player_repository import PlayerRepository

class PlayerService:
    """Player service class, layer between logic/ui modules and repository class"""

    def __init__(self, player_repository: PlayerRepository):
        """Constructor

        Args:
            player_repository (PlayerRepository): player repository
        """
        self._player_repository = player_repository

    def player_login(self, name: str) -> Player:
        """Assigns timestamp and creates player if does not exist.
        Otherwise updates last login time.

        Args:
            name (str): player name

        Returns:
            Player: player object or None in case of error.
        """
        now = datetime.now().timestamp()
        try:
            player = self._player_repository.find_player_by_name(name)
            if player is None:
                player = self._player_repository.add_player(
                    Player(name=name, last_login=now))
            else:
                player.set_login_time(now)
                self._player_repository.update_player(player)
            return player
        except Exception:
            return None
