class Dealer(Player):
    """Creates a dealer"""

    def deal_cards(self, deck: DeskCard) -> None:
        """Deal cards based on the dealer's rule"""
        while self.count < 21:
            card = deck.get_card()
            if card.get_value() + self.count <= 21:
                self.hand = card
            else:
                break


class Game:
    """Describes the game process"""

    def __init__(self, player_name: str) -> None:
        self.cards = DeskCard()
        self.player = Player(name=player_name)
        self.dealer = Dealer(name="Dealer")

    def start(self) -> None:
        """Deal 2 cards to the player and display information about their cards"""
        self.player.hand = self.cards.get_card()
        self.player.hand = self.cards.get_card()
        self.dealer.hand = self.cards.get_card()
        self.dealer.hand = self.cards.get_card()
        print(self.player.hand)

        while self.player.count < 21:
            answer = input("Do you want another card? (yes/no): ")
            if answer.lower() == "yes":
                self.player.hand = self.cards.get_card()
                print(self.player.hand)
            elif answer.lower() == "no":
                self.dealer.deal_cards(self.cards)
                break

        self.check_count()

    def display_info(self) -> str:
        """Display player and dealer information"""
        return f"\n{self.player.name}:\n{self.player.hand}\n{self.dealer.name}:\n{self.dealer.hand}"

    def check_count(self) -> None:
        """Determine the winner of the game"""
        if self.player.count > 21:
            print("You lose", self.display_info())
        elif self.dealer.count > 21 and self.player.count <= 21:
            print("You won!!!", self.display_info())
        elif self.dealer.count == self.player.count:
            print("Draw...", self.display_info())
        elif self.dealer.count > self.player.count:
            print("You lose", self.display_info())
        elif self.dealer.count < self.player.count:
            print("You won!!!", self.display_info())


def main() -> None:
    """Start the game"""
    while True:
        name = input("Your name?: ")
        game = Game(name)
        game.start()

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break


if __name__ == "__main__":
    main()
