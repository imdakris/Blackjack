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


class Dealer(Player):
    """Creates a dealer"""

    def get_cards(self, cards: DeskCard):
        """Rule"""
        while self.count < 21:
            _card = cards.get_card()
            if _card.get_value() + self.count <= 21:
                self.hand = _card
            else:
                break


class Game:
    """Describes the game process"""

    def __init__(self, player_name: str) -> None:
        self.cards = DeskCard()
        self.player = Player(name=player_name)
        self.dealer = Dealer(name="Dealer")

    def start(self) -> None:
        """We give 2 cards to the player and display information about his cards"""
        self.player.hand = self.cards.get_card()
        self.player.hand = self.cards.get_card()
        self.dealer.hand = self.cards.get_card()
        self.dealer.hand = self.cards.get_card()
        print(self.player.hand)
        while self.player.count < 21:
            answer = input("Card? y/n: ")
            if answer == "y":
                self.player.hand = self.cards.get_card()
                print(self.player.hand)
            elif answer == "n":
                self.dealer.get_cards(self.cards)
                break
        self.check_count()

    def print(self) -> str:
        """Print"""
        return f"\n{self.player.name}:\n{self.player.hand}\n{self.dealer.name}:\n{self.dealer.hand}"

    def check_count(self) -> None:
        """Determines the winner of the game"""
        if self.player.count > 21:
            print("You lose", self.print())
        elif self.dealer.count > 21 and self.player.count <= 21:
            print("You won!!!", self.print())
        elif self.dealer.count == self.player.count:
            print("Draw...", self.print())
        elif self.dealer.count > self.player.count:
            print("You lose", self.print())
        elif self.dealer.count < self.player.count:
            print("You won!!!", self.print())


def main() -> None:
    """Starts the game"""
    name = input("Your name?: ")
    game = Game(name)
    game.start()


if __name__ == "__main__":
    main()
