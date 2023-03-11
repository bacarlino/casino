from dataclasses import dataclass
import random


@dataclass(frozen=True)
class Outcome:
    """Represents a Roulette outcome that a bet is based on"""
    name: str
    odds: int

    def __str__(self) -> str:
        return f"{self.name} {self.odds}:1"
    
    def win_amount(self, amount: float) -> float:
        return self.odds * amount
    

class Bin(frozenset):
    """Represents a bin of a roulette wheel"""
    pass


class Wheel:
    """Represents a roulette wheel containing 38 bins"""
    def __init__(self) -> None:
        self.bins = tuple(Bin() for _ in range(38))
        self.rng = random.Random()

    def add_outcome(self, number: int, outcome: Outcome) -> None:
        """Add given outcome to bin at given index number"""
        new_bin = Bin(self.bins[number].union({outcome}))
        bins_list = list(self.bins)
        bins_list[number] = new_bin
        self.bins = tuple(bins_list)

    def choose(self) -> Bin:
        """Return a randomly selected Bin"""
        return self.rng.choice([bin for bin in self.bins])

    def get(self, bin: int) -> Bin:
        """Return the requested Bin"""
        return self.bins[bin]