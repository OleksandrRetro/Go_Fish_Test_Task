import random

from src.app.card import Card


class Deck:
    """
    Cards deck functionality.
    """

    def __init__(self) -> None:
        self.cards = []
        for suit in range(4):
            for rank in range(13):
                card = Card(suit, rank)
                self.cards.append(card)
        random.shuffle(self.cards)

    def __str__(self) -> str:
        """
        Deck string representation.
        :return: -> str
        """
        res: list = [str(card) for card in self.cards]
        return '\n'.join(res)

    def get_card_form_deck(self) -> Card:
        """
        Returns card from the deck.
        :return: -> Card
        """
        return self.cards.pop(0)

    def deck_size(self) -> int:
        """
        Returns deck size.
        :return: -> int
        """
        return len(self.cards)
