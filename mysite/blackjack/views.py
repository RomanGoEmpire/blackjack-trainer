import random
from django.shortcuts import render
from django.http import HttpResponse
from .models import Card
from .utils.evaluator import Evaluator

evaluator = Evaluator()


def index(request):
    return render(request, "index.html")


def cards(request):
    dealer_cards = [
        random.choice(Card.objects.exclude(value="back")),
        Card.objects.get(suit="card", value="back"),
    ]
    player_cards = generate_player_cards()
    split = player_cards[0].get_value() == player_cards[1].get_value()
    evaluator.player_cards = [player_cards[0].get_value(), player_cards[1].get_value()]
    evaluator.dealer_card = dealer_cards[0].get_value()

    return render(
        request,
        "cards.html",
        {"dealer_cards": dealer_cards, "player_cards": player_cards, "split": split},
    )


def generate_player_cards():
    sum = 21
    player_cards = []
    while sum == 21:
        player_cards = [
            random.choice(Card.objects.exclude(value="back")),
            random.choice(Card.objects.exclude(value="back")),
        ]
        sum = sum_card_values(player_cards)

    return player_cards


def sum_card_values(cards):
    return sum(card.get_value() for card in cards)


def tables(request):
    title = ["Hard Total", "Soft Total", "Splitting"]
    table_data = [
        evaluator.hard_total,
        evaluator.soft_total,
        evaluator.splitting,
    ]
    content = zip(title, table_data)
    print(table_data)
    return render(request, "tables.html", {"content": content})


def selected(request, option):
    is_correct, correct_choice = evaluator.evaluate_option(option)
    return render(
        request,
        "selected.html",
        {"is_correct": is_correct, "correct_choice": correct_choice, "option": option},
    )
