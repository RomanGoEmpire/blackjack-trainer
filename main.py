from flask import Flask, render_template, request
from handlers import Dealer
from config import Config

app = Flask(__name__)
app.config.from_object("config.Config")
dealer = Dealer()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dealer_cards")
def dealer_cards():
    return render_template("dynamic/cards.html", cards=dealer.dealer_cards())


@app.route("/player_cards")
def player_cards():
    return render_template("dynamic/cards.html", cards=dealer.player_cards())


@app.route("/cards")
def cards():
    dealer_cards = dealer.dealer_cards()
    player_cards = dealer.player_cards()
    print(dealer_cards, player_cards)
    return render_template(
        "dynamic/all_cards.html", dealer_cards=dealer_cards, player_cards=player_cards
    )


if __name__ == "__main__":
    app.run(debug=True)
