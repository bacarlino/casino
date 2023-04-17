import pytest

from roulette import Bet, Outcome

def test_bet():

    outcome1 = Outcome("Test 1", 1)
    outcome2 = Outcome("Test 2", 2)

    assert Bet(5, outcome1).win_amount() == 10
    assert Bet(10, outcome2).win_amount() == 30

    assert Bet(5, outcome1).lose_amount() == 5
    assert Bet(10, outcome2).lose_amount() == 10