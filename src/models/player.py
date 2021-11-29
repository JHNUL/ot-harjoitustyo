from datetime import datetime


class Player:
    def __init__(self, id_=None, name=None, last_login=None):
        self.id = id_
        self.name = name
        self.last_login = last_login

    def set_id(self, id_: int):
        self.id = id_

    def set_name(self, name: str):
        self.name = name

    def set_login_time(self, time: float):
        self.last_login = time

    def set_player(self, player: 'Player'):
        self.set_id(player.id)
        self.set_name(player.name)
        self.set_login_time(player.last_login)

    def __str__(self) -> str:
        last_lgn = datetime.fromtimestamp(self.last_login).isoformat()
        return f"Player {self.name} last logged {last_lgn}"
