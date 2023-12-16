class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_file_name(self):
        return f"{self.rank}_{self.suit}.svg"

    def value_as_number(self):
        if self.rank == "ace":
            return 11
        elif self.rank in ("jack", "queen", "king"):
            return 10
        else:
            return int(self.rank)
