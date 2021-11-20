from datetime import datetime


class Player:
    def __init__(self, id=None, playername=None, last_login=None):
        self.id = id
        self.playername = playername
        self.last_login = last_login

    def set_id(self, id: int):
        self.id = id

    def set_playername(self, playername: str):
        self.playername = playername

    def set_login_time(self, time: float):
        self.last_login = time

    def set_player(self, player: 'Player'):
        self.set_id(player.id)
        self.set_playername(player.playername)
        self.set_login_time(player.last_login)

    def __str__(self) -> str:
        return f"Player {self.playername} last logged {datetime.fromtimestamp(self.last_login).isoformat()}"
