import numpy as np
import os


class Evaluator:
    def __init__(self):
        print(os.getcwd())
        self.hard_total = np.genfromtxt("data/hard_total.csv", delimiter=",", dtype=str)
        self.soft_total = np.genfromtxt("data/soft_total.csv", delimiter=",", dtype=str)
        self.splitting = np.genfromtxt("data/splitting.csv", delimiter=",", dtype=str)

        self.dealer_cards = None
        self.player_cards = None

    def splitting(self, option):
        pass

    def soft_tolal(self, card, option):
        pass

    def hard_total(self, sum_player_cards, option):
        pass

    def evaluate_option(self, option):
        sum_player_cards = sum(self.player_cards)
        if sum_player_cards == 21:
            return "stand" == option
        if sum_player_cards > 8:
            return "hit" == option

        if self.player_cards[0] == self.player_cards[1]:
            return self.splitting(option)
        if 11 in self.player_cards:
            # card that is not ace
            card = (
                self.player_cards[0]
                if self.player_cards[0] != 11
                else self.player_cards[1]
            )
            return self.soft_tolal(card, option)
        else:
            return self.hard_total(sum_player_cards, option)
