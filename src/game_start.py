from src.app.deck import Deck
from src.app.game import Game
from src.app.player import Player

if __name__ == '__main__':
    game_instance: Game = Game()
    deck_instance: Deck = Deck()

    players: list = [Player("Player"), Player("Computer")]
    finish_game: int = 0
    active: int = 0
    not_active: int = 1

    game_instance.print_header()

    for i in range(7):
        players[0].get_card(deck_instance.get_card_form_deck())
        players[1].get_card(deck_instance.get_card_form_deck())

    while not finish_game:
        finish_game = game_instance.get_matched_cards_to_hand(players[active], players[not_active], deck_instance)

        if not finish_game:
            active, not_active = not_active, active
            input("\nOther player is active now. Please press [Enter] to continue.")

    game_instance.print_game_result(players)
