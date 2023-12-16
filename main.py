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


@app.route("/cards")
def cards():
    dealer_cards = dealer.deal_cards()
    player_cards = dealer.deal_cards()

    dealer_path = (dealer_cards[0].file_name(), "card_back.svg")
    player_path = (player_cards[0].file_name(), player_cards[1].file_name())

    evaluator.dealer_card = dealer_cards[0].value_as_number()
    evaluator.player_cards = (
        player_cards[0].value_as_number(),
        player_cards[1].value_as_number(),
    )

    if player_cards[0].value_as_number() == player_cards[1].value_as_number():
        options = render_template("dynamic/splitting_option.html")
    else:
        options = render_template("dynamic/standard_option.html")
    return render_template(
        "dynamic/all_cards.html",
        dealer_cards=dealer_path,
        player_cards=player_path,
        options=options,
    )


@app.route("/select_option")
def options():
    option = request.args.get("option")
    result = evaluator.evaluate_option(option)
    return render_template("dynamic/evaluation.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
