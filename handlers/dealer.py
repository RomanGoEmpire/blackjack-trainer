import random
from card import Card

SUITS = ("spades", "hearts", "diamonds", "clubs")
VALUES = ("ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king")


class Dealer:
    def __init__(self):
        pass

    def deal_cards(self):
        card_one = Card(random.choice(VALUES), random.choice(SUITS))
        card_two = Card(random.choice(VALUES), random.choice(SUITS))
        return card_one, card_two
