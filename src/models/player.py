from datetime import datetime


class Player:
    def __init__(self, id_=None, playername=None, last_login=None):
        self.id = id_
        self.playername = playername
        self.last_login = last_login

    def set_id(self, id_: int):
        self.id = id_

    def set_playername(self, playername: str):
        self.playername = playername

    def set_login_time(self, time: float):
        self.last_login = time

    def set_player(self, player: 'Player'):
        self.set_id(player.id)
        self.set_playername(player.playername)
        self.set_login_time(player.last_login)

    def __str__(self) -> str:
        last_lgn = datetime.fromtimestamp(self.last_login).isoformat()
        return f"Player {self.playername} last logged {last_lgn}"
