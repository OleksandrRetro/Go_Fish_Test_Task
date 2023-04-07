import pytest

from src.app.card import Card


@pytest.fixture()
def create_card():
    return Card(1, 1)


@pytest.mark.smoke
@pytest.mark.card
def test_card_str(create_card):
    assert str(create_card) == 'Three of Spades'


@pytest.mark.data_provider
@pytest.mark.card
@pytest.mark.smoke
@pytest.mark.parametrize("card, exp_rank",
                         [(Card(1, 11), 'King'),
                          (Card(2, 5), 'Seven'),
                          (Card(3, 7), 'Nine')]
                         )
def test_card_rank_equals(card, exp_rank):
    assert card.is_rank_equals(exp_rank)
