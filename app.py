from flask import Flask, render_template, request

from database.trade_db import (
    save_trade,
    get_all_trades,
    delete_trade
)

from database.portfolio_db import get_portfolio

from database.price_db import (
    save_price,
    get_all_prices
)

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

    return render_template(
        "trades.html",
        trades=get_all_trades()
    )


# Delete Trade
@app.route("/delete_trade/<int:trade_id>")
def remove_trade(trade_id):

    delete_trade(trade_id)

    return render_template(
        "trades.html",
        trades=get_all_trades()
    )


# Prices
@app.route("/prices", methods=["GET", "POST"])
def prices():

    if request.method == "POST":

        save_price(
            request.form.get("symbol"),
            request.form.get("price")
        )

    return render_template(
        "prices.html",
        prices=get_all_prices()
    )


# Scenario Analysis
@app.route("/scenario", methods=["GET", "POST"])
def scenario():

    result = None

    if request.method == "POST":

        portfolio = get_portfolio()

        symbol = request.form.get("symbol").upper()

        future_price = float(
            request.form.get("future_price")
        )

        if symbol in portfolio:

            shares = portfolio[symbol]["stock_qty"]

            avg_cost = 0

            if shares > 0:

                avg_cost = (
                    portfolio[symbol]["stock_cost"]
                    / shares
                )

            pnl = (
                future_price
                - avg_cost
            ) * shares

            result = {
                "symbol": symbol,
                "shares": shares,
                "avg_cost": round(avg_cost, 2),
                "future_price": future_price,
                "pnl": round(pnl, 2)
            }

    return render_template(
        "scenario.html",
        result=result
    )


# Heat Map
@app.route("/heatmap")
def heatmap():
    return """
    <h1>Heat Map</h1>

    <a href="/">Dashboard</a> |
    <a href="/portfolio">Portfolio</a> |
    <a href="/trades">Trades</a> |
    <a href="/prices">Prices</a> |
    <a href="/scenario">Scenario</a>

    <hr>

    <p>Heat Map Coming Soon</p>
    """


if __name__ == "__main__":
    app.run(debug=True)