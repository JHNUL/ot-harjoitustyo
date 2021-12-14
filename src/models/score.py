from models.player import Player


class Score:
    """Class representing score

    Attributes:
        value (int): score value
        player_id (int): indicates to which player this score belongs to
        timestamp (float): time when score was saved
        id_ (int): id of the score
    """

    def __init__(self, value: int, player_id: int = None, timestamp: float = None, id_: int = None):
        self.player_id = player_id
        self.timestamp = timestamp
        self.value = value
        self.id = id_

    def increase(self, amount: int = 1):
        """Method to increse score

        Args:
            amount (int, optional): amount to add. Defaults to 1.
        """
        self.value += amount

    def reset(self):
        """reset the score to zero"""
        self.value = 0

    def set_player_id(self, player: Player):
        """Setter for player id

        Args:
            player (Player): player object
        """
        self.player_id = player.id

    def set_timestamp(self, timestamp: float):
        """Setter for timestamp

        Args:
            timestamp (float): timestamp, unix format
        """
        self.timestamp = timestamp
