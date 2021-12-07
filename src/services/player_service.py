from datetime import datetime
from models.player import Player
from repositories.player_repository import PlayerRepository


class PlayerService:
    def __init__(self, player_repository: PlayerRepository):
        self._player_repository = player_repository

    def player_login(self, name: str) -> Player:
        now = datetime.now().timestamp()
        player = self._player_repository.find_player_by_name(name)
        if player is None:
            player = self._player_repository.add_player(
                Player(name=name, last_login=now))
        else:
            player.set_login_time(now)
            self._player_repository.update_player(player)
        return player
