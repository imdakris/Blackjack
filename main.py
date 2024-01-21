"""Writing a card game using classes"""
import random


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


class DeskCard:
    """Creates a deck of playing cards"""

    def __init__(self) -> None:
        _rank = "A23456789AJQK"
        _suit = "CDHS"  # clubs (♣), diamonds (♦), hearts (♥), spades (♠)
        self.__cards = [Card(r, s) for s in _suit for r in _rank]
        random.shuffle(self.__cards)
    
    def get_card(self)-> Card:
        '''To distribute playing cards'''
        return self.__cards.pop()
    
