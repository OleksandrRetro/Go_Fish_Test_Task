class Card:
    """
    Cards functionality.
    """

    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank

    suit_names: list = ['Diamonds', 'Spades', 'Clubs', 'Hearts']
    rank_names: list = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen',
                        'King', 'Ace']

    def __str__(self) -> str:
        """
        Cards string representation.
        :return: -> str
        """
        return f'{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}'

    def is_rank_equals(self, card_rank: str) -> int:
        """
        Checks whether card ranks are equals.
        :param card_rank: str
        :return: -> int
        """
        return 1 if str(Card.rank_names[self.rank]) == card_rank else 0
