
class Player:
    """Class representing player

    Attributes:
        id (int): unique id
        name (str): player name
        last_login (float): unix timestamp of last login
    """

    def __init__(self, id_: int = None, name: str = None, last_login: float = None):
        """Constructor

        Args:
            id_ (int, optional): player id. Defaults to None.
            name (str, optional): player name. Defaults to None.
            last_login (float, optional): last login time, unix timestamp. Defaults to None.
        """
        self.id = id_
        self.name = name
        self.last_login = last_login

    def set_id(self, id_: int):
        """Setter for id

        Args:
            id_ (int): player id
        """
        self.id = id_

    def set_name(self, name: str):
        """Setter for name

        Args:
            name (str): player name
        """
        self.name = name

    def set_login_time(self, time: float):
        """Setter for login time

        Args:
            time (float): login time, unix timestamp
        """
        self.last_login = time

    def set_player(self, player: 'Player'):
        """Sets all player attributes

        Args:
            player (Player): Player object
        """
        self.set_id(player.id)
        self.set_name(player.name)
        self.set_login_time(player.last_login)
