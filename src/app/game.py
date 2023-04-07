from src.app.card import Card
from src.app.deck import Deck
from src.app.player import Player


class Game:

    def print_header(self) -> None:
        print("\n" + "*" * 30)
        print("Test task for [Go FISH!] game.")
        print(f"Choose cards by using: {Card.rank_names}")
        print("*" * 30)
        input("\nPress [Enter] to start the game.")

    def print_round_statistic(self, player: Player, computer: Player, deck: Deck) -> None:
        print(player)
        print(computer)
        print("\nDeck size is: %s" % deck.deck_size())

    def get_asked_rank(self, player: Player, computer: Player, deck: Deck) -> str:
        Game().print_round_statistic(player, computer, deck)
        rank_to_ask: str = input("\nPlease ask a card: ")
        print()
        return rank_to_ask

    def get_matched_cards_to_hand(self, player: Player, computer: Player, deck: Deck):
        asked_card: str = self.get_asked_rank(player, computer, deck)
        computer_matches: list = computer.get_matched_cards(asked_card)
        if computer_matches:
            print("The card, you've asked matched.")
            for i in reversed(computer_matches):
                print(computer.hand[i])
                player.get_card(computer.hand[i])
                computer.remove_card(computer.hand[i])
            player.check_cards_for_book()
            input("Press [Enter] to continue.")
            if Game().win_condition(player, computer, deck):
                return Game().win_condition(player, computer, deck)
            else:
                return Game().get_matched_cards_to_hand(player, computer, deck)
        else:
            print("GO FISH!")
            if deck.deck_size() > 0:
                taken_card: Card = deck.get_card_form_deck()
                computer.get_card(taken_card)
                print(f"You get the {taken_card}")
                computer.check_cards_for_book()
                if taken_card.is_rank_equals(asked_card):
                    print("You got the card you asked before. Please ask a card again")
                    input("Press [Enter] to continue.")
                    if Game().win_condition(player, computer, deck):
                        return Game().win_condition(player, computer, deck)
                    else:
                        return Game().get_matched_cards_to_hand(player, computer, deck)
            else:
                print("Other player is active now.")
                return Game().win_condition(player, computer, deck)

    def win_condition(self, player: Player, computer: Player, deck: Deck) -> int:
        return 1 if not deck.deck_size() > 0 and not player.hand and not computer.hand else 0

    def print_game_result(self, players: list) -> None:
        print(f"{players[0].name}'s score: {players[0].score}")
        print(f"{players[1].name}'s score: {players[1].score}")

        if players[0].score > players[1].score:
            print(f"{players[0].name} wins!")
        elif players[1].score > players[0].score:
            print(f"{players[1].name} wins!")
        else:
            print("Nobody wins. The scores are equals.")
