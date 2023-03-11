from roulette import Outcome, Wheel


def test_wheel_sequence():
    wheel = Wheel()
    wheel.add_outcome(8, Outcome("test", 1))
    wheel.rng.seed(1)
    assert Outcome("test", 1) in wheel.choose()
