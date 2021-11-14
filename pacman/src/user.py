class User:
    def __init__(self):
        self._logged_in_timestamp = None
        self._username = None
        self._playername = None

    def get_username(self):
        return self._username

    def get_playername(self):
        return self._playername
    
    def get_login_time(self):
        return self._logged_in_timestamp
