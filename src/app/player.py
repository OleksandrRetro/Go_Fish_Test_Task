from collections import Counter

from src.app.card import Card


class Player:
    """
    Player functionality.
    """

    def __init__(self, name: str) -> None:
        """
        Creates player instance.
        :param name: str
        """
        self.name = name
        self.hand = []
        self.books = 0

    def __str__(self) -> str:
        """
        Player string representation.
        Returns all player cards.
        :return: -> str
        """
        print("\n\n" + "*" * 30 + "\nName: %s | Books: %d \nHand:" % (self.name, self.books))
        res: list = [str(card) for card in self.hand]
        return '\n'.join(res)

    def get_matched_cards(self, card_rank: str) -> list:
        """
        Returns matched cards list.
        :param card_rank:
        :return: -> list
        """
        matches: list = []
        count: int = 0
        for i in self.hand:
            if i.is_rank_equals(card_rank):
                matches.append(count)
            count += 1
        return matches if matches else print("The card [%s] is not matched." % card_rank)

    def get_card(self, card: Card) -> None:
        self.hand.append(card)

    def remove_card(self, card: Card) -> None:
        self.hand.remove(card)

    def check_cards_for_book(self) -> None:
        """
        Verifies and creates a book from 4 cards with the same rank if exists.
        :return: -> None
        """
        ranks: list = []
        for i in range(len(self.hand)):
            ranks.append(self.hand[i].rank)

        count_ranks: Counter = Counter(ranks)
        most_common_cards: list = count_ranks.most_common()
        matches: list = []
        for element in most_common_cards:
            if element[1] == 4:
                print("Cards in your hand to make a book: ")
                self.books += 1
                matches.append(element[0])
                print(str(Card.rank_names[element[0]]))

        remove_cards: list = []
        for item in self.hand:
            if item.rank in matches:
                remove_cards.append(item)

        for j in range(len(remove_cards)):
            self.remove_card(remove_cards[j])

        if not remove_cards:
            print("You have no cards to make a book.")
