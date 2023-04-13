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
    """Creates available Outcome instances and adds them to a Bin index"""
    def __init__(self, wheel: Wheel):
        self.wheel = wheel

    def build_bins(self):
        """Run all algorithm methods to create outcomes and send to the wheel"""
        self.straight_bets()
        self.split_bets()
        self.street_bets()
        self.corner_bets()
        self.line_bets()
        self.dozen_bets()
        self.column_bets()
        self.even_money_bets()
        self.five_bet()

    def straight_bets(self) -> None:
        """Create 38 straight bet Outcomes and send to the wheel"""
        for bin_index in range(37):
            self.wheel.add_outcome(bin_index, Outcome(f"Straight Bet {bin_index}", 35))
        self.wheel.add_outcome(37, Outcome("Straight Bet 0-0", 35))

    def split_bets(self) -> None:
        """Create all split bet Outcomes and send to the wheel"""

        for row in range(12):
            first_column = 3*row + 1
            first_outcome = Outcome(
                f"Split Bet {first_column}-{first_column+1}", 17)
            self.wheel.add_outcome(first_column, first_outcome)
            self.wheel.add_outcome(first_column+1, first_outcome)

            second_column = 3*row + 2
            second_outcome =  Outcome(
                f"Split Bet {second_column}-{second_column+1}", 17)
            self.wheel.add_outcome(second_column, second_outcome)
            self.wheel.add_outcome(second_column+1, second_outcome)

        for num in range(1, 34):
            third_outcome = Outcome(f"Split Bet {num}-{num+3}", 17)
            self.wheel.add_outcome(num, third_outcome)
            self.wheel.add_outcome(num+3, third_outcome)

    def street_bets(self) -> None:
        """Create (12) street bets and send to the wheel"""

        for row in range(12):
            num = (3*row) + 1
            outcome = Outcome(
                f"Street Bet {num}-{num+1}-{num+2}", 11)
            
            for x in range(3):
                self.wheel.add_outcome(num + x, outcome)

    def corner_bets(self) -> None:
        """Create the corner bets and send to the wheel"""
        for row in range(11):
            column_1_number = 3*row + 1
            outcome_1 = Outcome(
                f"Corner Bet {column_1_number}-{column_1_number + 1}-"
                f"{column_1_number + 3}-{column_1_number + 4}", 8)    
            for x in [0, 1, 3, 4]:
                self.wheel.add_outcome(column_1_number + x, outcome_1)

            column_2_number = 3*row + 2
            outcome_2 = Outcome(
                f"Corner Bet {column_2_number}-{column_2_number + 1}-"
                f"{column_2_number + 3}-{column_2_number + 4}", 8)
            for x in [0, 1, 3, 4]:
                self.wheel.add_outcome(column_2_number + x, outcome_2)

    def line_bets(self) -> None:
        """Create line bets and send to the wheel"""
        for row in range(11):
            number = 3*row + 1
            outcome = Outcome(
                f"Line Bet {number}-{number + 1}-{number + 2}-"
                f"{number + 3}-{number + 4}-{number + 5}", 5)
            for x in range(6):
                self.wheel.add_outcome(number + x, outcome)
    
    def dozen_bets(self) -> None:
        """Create dozen bets and send to the wheel"""
        for dozen in range(3):
            outcome = Outcome(f"Dozen Bet {dozen + 1}", 2)
            for x in range(12):
                self.wheel.add_outcome(12*dozen + x + 1, outcome)

    def column_bets(self) -> None:
        """Create column bets and send to the wheel"""
        for column in range(3):
            outcome = Outcome(f"Column Bet {column + 1}", 2)
            for row in range(12):
                self.wheel.add_outcome(3*row + column + 1, outcome)

    def even_money_bets(self) -> None:
        """Create even money bets and send to the wheel"""
        red = Outcome("Red Bet", 1)
        black = Outcome("Black Bet", 1)
        even = Outcome("Even Bet", 1)
        odd = Outcome("Odd Bet", 1)
        high = Outcome("High Bet", 1)
        low = Outcome("Low Bet", 1)

        for num in range(1, 37):
            if 1 <= num < 19:
                self.wheel.add_outcome(num, low)
            else:
                self.wheel.add_outcome(num, high)
            if num % 2 == 0:
                self.wheel.add_outcome(num, even)
            else:
                self.wheel.add_outcome(num, odd)
            if num in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 
                       21, 23, 25, 27, 30, 32, 34, 36]:
                self.wheel.add_outcome(num, red)
            else:
                self.wheel.add_outcome(num, black)

    def five_bet(self) -> None:
        """Create the five bet and send to the wheel"""
        outcome = Outcome("Five Bet", 6)
        for bin in [0, 37, 1, 2, 3]:
            self.wheel.add_outcome(bin, outcome)
