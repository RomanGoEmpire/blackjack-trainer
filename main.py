from flask import Flask, render_template, request
from handlers import Dealer, Evaluator
from config import Config

app = Flask(__name__)
app.config.from_object("config.Config")
dealer = Dealer()
evaluator = Evaluator()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dealer_cards")
def dealer_cards():
    cards = dealer.deal_cards()
    evaluator.dealer_cards = (cards[0].value_as_number(), cards[1].value_as_number())
    files = (cards[0].get_file_name(), "card_back.svg")
    return render_template("dynamic/cards.html", cards=files)


@app.route("/player_cards")
def player_cards():
    cards = dealer.deal_cards()
    evaluator.player_cards = (cards[0].value_as_number(), cards[1].value_as_number())
    files = (cards[0].get_file_name(), cards[1].get_file_name())
    return render_template("dynamic/cards.html", cards=files)


@app.route("/cards")
def cards():
    dealer_cards = dealer.dealer_cards()
    player_cards = dealer.player_cards()
    print(dealer_cards, player_cards)
    return render_template(
        "dynamic/all_cards.html", dealer_cards=dealer_cards, player_cards=player_cards
    )


@app.route("/select_option")
def options():
    option = request.args.get("option")
    result = evaluator.evaluate_option(option)
    return render_template("dynamic/evaluation.html", option=option, result=result)


if __name__ == "__main__":
    app.run(debug=True)
