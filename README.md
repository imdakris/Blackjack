# Blackjack

# If you want to reduce the difficulty of the game

```python
class Dealer(Player):
    """Creates a dealer"""

    def get_cards(self, cards: DeskCard):
        """Rule"""
        while self.count < 18:
            self.hand = cards.get_card()
```

# Replace the block below

```python
class Dealer(Player):
    """Creates a dealer"""
    def get_cards(self, cards: DeskCard):
        """Rule"""
        while self.count < 21:
            _card = cards.get_card()
            if _card.get_value + self.count <= 21:
                self.hand = _card
            else:
                break
```
