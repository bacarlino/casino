import pytest

from roulette import Bin, Outcome

def test_bin():
    o1 = Outcome("0", 35)
    o2 = Outcome("00", 35)
    o3 = Outcome("0-00-1-2-3", 16)

    b = Bin([o1, o3])
    b = Bin((o2, o3))

