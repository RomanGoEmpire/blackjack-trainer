import random

suits = ("spades", "hearts", "diamonds", "clubs")
values = ("ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king")


class Dealer:
    def __init__(self):
        pass

    def dealer_cards(self):
        card = f"{random.choice(suits)}_{random.choice(values)}"
        return card, "backside"

    def player_cards(self):
        card_one = f"{random.choice(suits)}_{random.choice(values)}"
        card_two = f"{random.choice(suits)}_{random.choice(values)}"
        return card_one, card_two
