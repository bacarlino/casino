import pytest

from roulette import Outcome, Wheel

@pytest.fixture
def wheel_with_outcome():
    wheel = Wheel()
    wheel.add_outcome(8, Outcome("test", 1))
    return wheel
    
def test_wheel_sequence(wheel_with_outcome):
    wheel_with_outcome.rng.seed(1)
    assert Outcome("test", 1) in wheel_with_outcome.choose()


def test_get_outcome(wheel_with_outcome):
    assert wheel_with_outcome.get_outcome("test") == Outcome("test", 1)