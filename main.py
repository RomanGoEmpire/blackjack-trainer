from flask import Flask, render_template, request
from handlers import Dealer, Evaluator, Statistics
from config import Config

app = Flask(__name__)
app.config.from_object("config.Config")
dealer = Dealer()
evaluator = Evaluator()
statistics = Statistics()


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
        "cards.html",
        dealer_cards=dealer_path,
        player_cards=player_path,
        options=options,
        statistics=current_statistics(),
    )


@app.route("/select_option")
def options():
    option = request.args.get("option")
    is_correct, answer = evaluator.evaluate_option(option)

    statistics.update(is_correct)

    return render_template(
        "dynamic/evaluation.html", is_correct=is_correct, answer=answer
    )


@app.route("/statistics")
def current_statistics():
    return render_template(
        "dynamic/statistics.html",
        total=statistics.total,
        correct=statistics.correct,
        wrong=statistics.wrong,
        percentage=statistics.percentage(),
    )


@app.route("/tables")
def hard_total():
    content = [
        ("Hard Total", evaluator.hard_total),
        ("Soft Total", evaluator.soft_total),
        ("Splitting", evaluator.splitting),
    ]
    return render_template(
        "tables.html",
        content=content,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)
