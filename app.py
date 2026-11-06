from flask import Flask, render_template, request

from database.trade_db import (
    save_trade,
    get_all_trades,
    delete_trade
)

from database.portfolio_db import get_portfolio

app = Flask(__name__)


# Dashboard
@app.route("/")
def dashboard():
    return render_template("index.html")


# Portfolio
@app.route("/portfolio")
def portfolio():

    portfolio = get_portfolio()

    return render_template(
        "portfolio.html",
        portfolio=portfolio
    )


# Trades
@app.route("/trades", methods=["GET", "POST"])
def trades():

    if request.method == "POST":

        save_trade(
            request.form.get("symbol"),
            request.form.get("asset_type"),
            request.form.get("side"),
            request.form.get("quantity"),
            request.form.get("price"),
            request.form.get("strike"),
            request.form.get("expiry")
        )

    trades = get_all_trades()

    return render_template(
        "trades.html",
        trades=trades
    )


# DELETE TRADE
@app.route("/delete_trade/<int:trade_id>")
def remove_trade(trade_id):

    delete_trade(trade_id)

    return render_template(
        "trades.html",
        trades=get_all_trades()
    )


# Scenario Analysis
@app.route("/scenario")
def scenario():
    return """
    <h1>Scenario Analysis</h1>

    <a href="/">Dashboard</a> |
    <a href="/portfolio">Portfolio</a> |
    <a href="/trades">Trades</a> |
    <a href="/heatmap">Heat Map</a>

    <hr>

    <p>Scenario Engine Coming Soon</p>
    """


# Heat Map
@app.route("/heatmap")
def heatmap():
    return """
    <h1>Heat Map</h1>

    <a href="/">Dashboard</a> |
    <a href="/portfolio">Portfolio</a> |
    <a href="/trades">Trades</a> |
    <a href="/scenario">Scenario</a>

    <hr>

    <p>Heat Map Coming Soon</p>
    """


if __name__ == "__main__":
    app.run(debug=True)