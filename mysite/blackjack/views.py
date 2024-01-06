import random
from django.shortcuts import render
from django.http import HttpResponse
from .models import Card
from .utils.evaluator import Evaluator

evaluator = Evaluator()


def index(request):
    return render(request, "index.html")


def cards(request):
    back = Card.objects.get(suit="card", value="back")
    dealer_cards = [random.choice(Card.objects.exclude(value="back")), back]

    sum = 21
    player_cards = []
    while sum == 21:
        player_cards = [
            random.choice(Card.objects.exclude(value="back")),
            random.choice(Card.objects.exclude(value="back")),
        ]
        sum = player_cards[0].get_value() + player_cards[1].get_value()

    return render(
        request,
        "cards.html",
        {"dealer_cards": dealer_cards, "player_cards": player_cards},
    )


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
