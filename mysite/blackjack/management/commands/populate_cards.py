from django.core.management.base import BaseCommand
from blackjack.models import Card

SUITS = ("spades", "hearts", "diamonds", "clubs")
VALUES = ("ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king")

class Command(BaseCommand):
    help = 'Populates the database with all cards'

    def handle(self, *args, **options):
        Card.objects.all().delete()
        for suit in SUITS:
            for value in VALUES:
                image_path = f'images/cards/{suit}_{value}.svg'
                print(image_path)
                Card.objects.create(suit=suit, value=value, image=image_path)
        Card.objects.create(suit="card", value="back", image="images/cards/card_back.svg")
