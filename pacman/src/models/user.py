class User:
    def __init__(self, id=None, username=None, playername=None, login_time=None):
        self.id = id
        self.username = username
        self.playername = playername
        self.login_time = login_time

    def set_id(self, id):
        self.id = id

    def set_username(self, username):
        self.username = username

    def set_playername(self, playername):
        self.playername = playername

    def set_login_time(self, time):
        self.login_time = time

    def __str__(self) -> str:
        return f"{self.username} {self.playername} {self.login_time}"
