class Player:
    def __init__(self, id=None, playername=None, screenname=None, login_time=None):
        self.id = id
        self.playername = playername
        self.screenname = screenname
        self.login_time = login_time

    def set_id(self, id):
        self.id = id

    def set_playername(self, playername):
        self.playername = playername

    def set_screenname(self, screenname):
        self.screenname = screenname

    def set_login_time(self, time):
        self.login_time = time

    def set_player(self, player: 'Player'):
        self.set_id(player.id)
        self.set_playername(player.playername)
        self.set_screenname(player.screenname)
        self.set_login_time(player.login_time)

    def __str__(self) -> str:
        return f"Player {self.screenname} with playername {self.playername} last logged {self.login_time}"
