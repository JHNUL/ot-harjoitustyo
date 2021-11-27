class Score:
    def __init__(self, score, player_id=None, score_timestamp=None, id_=None):
        self.player_id = player_id
        self.score_timestamp = score_timestamp
        self.score = score
        self.id = id_

    def increase(self, amount=1):
        self.score += amount
