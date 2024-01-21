"""Writing a card game using classes"""


class Card:
    """Description of playing card"""

    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit

    def get_value(self) -> int:
        """Returns playing card points"""
        if self.rank in "AJQK":  # "Ace, Jack, Queen, King"
            return 10
        else:
            return " A23456789".index(self.rank)

    def get_rank(self):
        """Displays playing card information"""
        return f"{self.suit}{self.rank}"
