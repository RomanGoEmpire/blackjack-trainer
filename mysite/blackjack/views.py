from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")

def cards(request):
    dealercards = ['club_2','card_back']
    playercards = ['club_3','club_4']
    return render(request, "cards.html", {
        "dealer_cards": dealercards,
        "player_cards": playercards
    })
        

def tables(request):
    return render(request, "tables.html")