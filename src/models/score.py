class Score:
    def __init__(self, value, player_id=None, timestamp=None, id_=None):
        self.player_id = player_id
        self.timestamp = timestamp
        self.value = value
        self.id = id_

    def increase(self, amount=1):
        self.value += amount

    def reset(self):
        self.value = 0
