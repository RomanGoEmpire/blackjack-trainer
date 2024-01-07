import random
from django.shortcuts import render
from django.http import HttpResponse
from .models import Card
from .utils.evaluator import Evaluator

evaluator = Evaluator()


###### ! VIEW FUNCTIONS ########


def index(request):
    return render(request, "index.html")


# * Games


def games(request):
    return render(request, "games.html")


def practice(request):
    dealer_cards, player_cards, split = generate_cards()
    return render(
        request,
        "games/practice.html",
        {
            "dealer_cards": dealer_cards,
            "player_cards": player_cards,
            "split": split,
            "mode": "practice",
        },
    )


def selected(request, option, mode):
    is_correct, correct_choice = evaluator.evaluate_option(option)
    return render(
        request,
        "selected.html",
        {
            "is_correct": is_correct,
            "correct_choice": correct_choice,
            "option": option,
            "mode": mode,
        },
    )


# * Stats


def stats(request):
    return render(request, "stats.html")


def tables(request):
    title = ["Hard Total", "Soft Total", "Splitting"]
    table_data = [
        evaluator.hard_total,
        evaluator.soft_total,
        evaluator.splitting,
    ]
    content = zip(title, table_data)
    return render(request, "tables.html", {"content": content})


###### ! HELPER FUNCTIONS ########


def generate_cards():
    # Generating dealer cards
    dealer_cards = [
        random.choice(Card.objects.exclude(value="back")),
        Card.objects.get(suit="card", value="back"),
    ]
    # Generating player cards
    sum_cards = 21
    player_cards = []
    while sum_cards == 21:
        player_cards = [
            random.choice(Card.objects.exclude(value="back")),
            random.choice(Card.objects.exclude(value="back")),
        ]
        sum_cards = sum(card.get_value() for card in player_cards)
    # Check if player can split
    split = player_cards[0].get_value() == player_cards[1].get_value()
    # Set evaluator cards that will be used later when evaluating the option
    evaluator.player_cards = [player_cards[0].get_value(), player_cards[1].get_value()]
    evaluator.dealer_card = dealer_cards[0].get_value()

    return dealer_cards, player_cards, split
