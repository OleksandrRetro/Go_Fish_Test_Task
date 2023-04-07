import pytest

from src.app.card import Card
from src.app.deck import Deck


@pytest.fixture()
def create_deck():
    return Deck()


@pytest.mark.smoke
@pytest.mark.deck
def test_deck_size(create_deck):
    assert create_deck.deck_size() == 52


@pytest.mark.smoke
@pytest.mark.deck
def test_get_card_from_deck(create_deck):
    deck: Deck = create_deck
    get_card: Card = deck.get_card_form_deck()
    assert str(get_card) not in str(deck)
    assert deck.deck_size() == 51
