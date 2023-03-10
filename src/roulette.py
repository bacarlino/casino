from dataclasses import dataclass


@dataclass(frozen=True)
class Outcome:
    """Represents a Roulette outcome that a bet is based on"""
    name: str
    odds: int

    def __str__(self):
        return f"{self.name} {self.odds}:1"
    
    def win_amount(self, amount: float) -> float:
        return self.odds * amount
    

class Bin(frozenset):
    """Represents a bin of a roulette wheel"""
    pass