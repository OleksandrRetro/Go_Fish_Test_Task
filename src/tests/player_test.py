import pytest

from src.app.deck import Deck
from src.app.player import Player

PLAYER_NAME = "Test_player_name"


@pytest.fixture()
def create_empty_player():
    return Player(PLAYER_NAME)


@pytest.mark.smoke
@pytest.mark.player
def test_empty_player(create_empty_player):
    player: Player = create_empty_player
    assert player.books == 0
    assert len(player.hand) == 0
    assert player.name == PLAYER_NAME


@pytest.fixture()
def create_filled_player():
    player: Player = Player(PLAYER_NAME)
    deck: Deck = Deck()
    for i in range(7):
        player.get_card(deck.get_card_form_deck())
    return player


@pytest.mark.smoke
@pytest.mark.player
def test_player_parameters(create_filled_player):
    player: Player = create_filled_player
    assert player.books == 0
    assert len(player.hand) == 7
    assert player.name == PLAYER_NAME
