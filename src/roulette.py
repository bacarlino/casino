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
    

class BinBuilder:
    """Creates available Outcome(s) instances and adds them to a Bin index"""
    def __init__(self, wheel: Wheel):
        self.wheel = wheel

    def build_bins(self):
        pass

    def straight_bet(self) -> None:
        """Create 38 straight bet Outcomes and send to the wheel"""
        for bin_index in range(37):
            self.wheel.add_outcome(bin_index, Outcome(f"Straight Bet {bin_index}", 35))
        self.wheel.add_outcome(37, Outcome("Straight Bet 0-0"), 35)

    def split_bet(self) -> None:
        """Create all split bet Outcomes and send to the wheel"""

        for row in range(12):

            
            first_column = (3 * row) + 1
            first_outcome = Outcome(f"({first_column},{first_column+1}) Split Bet", 17)
            self.wheel.add_outcome(first_column, first_outcome)
            self.wheel.add_outcome(first_column+1, first_outcome)

            second_column = (3 * row) + 3
            second_outcome =  Outcome(f"({second_column},{second_column+1}) Split Bet", 17)
            self.wheel.add_outcome(second_column, second_outcome)
            self.wheel.add_outcome(second_column+1, second_outcome)

        



            


        