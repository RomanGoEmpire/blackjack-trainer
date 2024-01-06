import numpy as np
import os
import os


class Evaluator:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(base_dir)
        paths = [
            os.path.join(base_dir, "data/hard_total.csv"),
            os.path.join(base_dir, "data/soft_total.csv"),
            os.path.join(base_dir, "data/splitting.csv"),
        ]
        self.hard_total = np.genfromtxt(paths[0], delimiter=",", dtype=str)
        self.soft_total = np.genfromtxt(paths[1], delimiter=",", dtype=str)
        self.splitting = np.genfromtxt(paths[2], delimiter=",", dtype=str)

        self.dealer_card: int = None
        self.player_cards: list = None

    def eval_splitting(self, option):
        correct_choice = self.splitting[self.player_cards[0] - 1][self.dealer_card - 1]
        return correct_choice == option, correct_choice

    def eval_soft_total(self, card, option):
        correct_choice = self.soft_total[card - 1][self.dealer_card - 1]
        return correct_choice == option, correct_choice

    def eval_hard_total(self, sum_player_cards, option):
        if sum_player_cards < 8:
            sum_player_cards = 8
        elif sum_player_cards > 17:
            sum_player_cards = 17
        correct_choice = self.hard_total[sum_player_cards - 7][self.dealer_card - 1]
        return correct_choice == option, correct_choice

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
            return self.eval_soft_total(card, option)
        else:
            return self.eval_hard_total(sum_player_cards, option)
