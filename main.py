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

    def get_rank(self) -> str:
        """Displays playing card information"""
        return f"{self.suit}{self.rank}"


class DeskCard:
    """Creates a deck of playing cards"""

    def __init__(self) -> None:
        _rank = "A23456789AJQK"
        _suit = "CDHS"  # clubs (♣), diamonds (♦), hearts (♥), spades (♠)
        self.__cards = [Card(r, s) for s in _suit for r in _rank]
        random.shuffle(self.__cards)

    def get_card(self) -> Card:
        """To distribute playing cards"""
        return self.__cards.pop()


class Player:
    """Creates and describes a player"""

    def __init__(self, name: str) -> None:
        self._hand = []
        self.count = 0
        self.name = name

    @property
    def hand(self) -> str:
        """Informs the player about his cards and points"""
        return f"Playing cards in hand: {self._hand}; Points you have:{self.count}"

    @hand.setter
    def hand(self, card: Card) -> None:
        self.count += card.get_value()
        self._hand.append(card.get_rank())


class Game:
    """Describes the game process"""

    def __init__(self, player_name: str) -> None:
        self.cards = DeskCard()
        self.player = Player(name=player_name)

    def start(self) -> None:
        """We give 2 cards to the player and display information about his cards"""
        self.player.hand = self.cards.get_card()
        self.player.hand = self.cards.get_card()
        print(self.player.hand)
