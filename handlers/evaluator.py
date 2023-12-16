import numpy as np
import os


class Evaluator:
    def __init__(self):
        self.hard_total = np.genfromtxt("data/hard_total.csv", delimiter=",", dtype=str)
        self.soft_total = np.genfromtxt("data/soft_total.csv", delimiter=",", dtype=str)
        self.splitting = np.genfromtxt("data/splitting.csv", delimiter=",", dtype=str)

        self.dealer_card = None
        self.player_cards = None

    def eval_splitting(self, option):
        correct_choice = self.splitting[self.player_cards[0] - 1][self.dealer_card - 1]
        return correct_choice == option

    def eval_soft_tolal(self, card, option):
        correct_choice = self.soft_total[card - 1][self.dealer_card - 1]
        return correct_choice == option

    def eval_hard_total(self, sum_player_cards, option):
        if sum_player_cards < 8:
            sum_player_cards = 8
        elif sum_player_cards > 17:
            sum_player_cards = 17
        correct_choice = self.hard_total[sum_player_cards - 7][self.dealer_card - 1]
        return correct_choice == option

    def evaluate_option(self, option):
        sum_player_cards = sum(self.player_cards)

        if self.player_cards[0] == self.player_cards[1]:
            return self.eval_splitting(option)
        if 11 in self.player_cards:
            # card that is not ace
            card = (
                self.player_cards[0]
                if self.player_cards[0] != 11
                else self.player_cards[1]
            )
            return self.eval_soft_tolal(card, option)
        else:
            return self.eval_hard_total(sum_player_cards, option)
