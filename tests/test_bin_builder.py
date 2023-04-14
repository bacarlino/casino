import pytest

from roulette import BinBuilder, Outcome, Wheel

def test_bin_builder():

    wheel = Wheel()
    BinBuilder(wheel).build_bins()

    assert Outcome("Straight Bet 0", 35) in wheel.get(0)
    assert Outcome("Straight Bet 0-0", 35) in wheel.get(37)
    assert Outcome("Straight Bet 1", 35) in wheel.get(1)
    assert Outcome("Straight Bet 36", 35) in wheel.get(36)

    assert Outcome("Split Bet 1-2", 17) in wheel.get(1)
    assert Outcome("Split Bet 1-4", 17) in wheel.get(1)
    assert Outcome("Split Bet 33-36", 17) in wheel.get(36)
    assert Outcome("Split Bet 35-36", 17) in wheel.get(36)

    assert Outcome("Street Bet 1-2-3", 11) in wheel.get(1)
    assert Outcome("Street Bet 34-35-36", 11) in wheel.get(36)

    assert Outcome("Corner Bet 1-2-4-5", 8) in wheel.get(1)
    assert Outcome("Corner Bet 1-2-4-5", 8) in wheel.get(4)
    assert Outcome("Corner Bet 4-5-7-8", 8) in wheel.get(4)
    assert Outcome("Corner Bet 1-2-4-5", 8) in wheel.get(5)
    assert Outcome("Corner Bet 2-3-5-6", 8) in wheel.get(5)
    assert Outcome("Corner Bet 4-5-7-8", 8) in wheel.get(5)
    assert Outcome("Corner Bet 5-6-8-9", 8) in wheel.get(5)
    
    assert len([outcome for outcome in wheel.get(1)
            if "Line Bet" in outcome.name]) == 1
    assert len([outcome for outcome in wheel.get(4)
            if "Line Bet" in outcome.name]) == 2
    
    assert Outcome("Dozen Bet 1", 2) in wheel.get(1)
    assert Outcome("Dozen Bet 2", 2) in wheel.get(17)
    assert Outcome("Dozen Bet 3", 2) in wheel.get(36)

    assert Outcome("Column Bet 1", 2) in wheel.get(1)
    assert Outcome("Column Bet 2", 2) in wheel.get(17)
    assert Outcome("Column Bet 3", 2) in wheel.get(36)

    assert Outcome("Low Bet", 1) in wheel.get(1)
    assert Outcome("Low Bet", 1) in wheel.get(17)
    assert Outcome("Low Bet", 1) in wheel.get(18)

    assert Outcome("High Bet", 1) in wheel.get(36)

    assert Outcome("Red Bet", 1) in wheel.get(1)
    assert Outcome("Red Bet", 1) in wheel.get(18)
    assert Outcome("Red Bet", 1) in wheel.get(36)

    assert Outcome("Black Bet", 1) in wheel.get(17)

    assert Outcome("Even Bet", 1) in wheel.get(18)
    assert Outcome("Even Bet", 1) in wheel.get(36)
    
    assert Outcome("Odd Bet", 1) in wheel.get(1)
    assert Outcome("Odd Bet", 1) in wheel.get(17)

    assert Outcome("Five Bet", 6) in wheel.get(0)
    assert Outcome("Five Bet", 6) in wheel.get(37)



    
    
        