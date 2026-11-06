import sqlite3


def get_portfolio():

    conn = sqlite3.connect("database/trades.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            symbol,
            asset_type,
            side,
            quantity,
            price
        FROM trades
    """)

    rows = cursor.fetchall()

    conn.close()

    portfolio = {}

    for symbol, asset_type, side, quantity, price in rows:

        if symbol not in portfolio:

            portfolio[symbol] = {
                "stock_qty": 0,
                "stock_cost": 0,

                "call_qty": 0,
                "call_cost": 0,

                "put_qty": 0,
                "put_cost": 0
            }

        qty = float(quantity)
        price = float(price)

        if asset_type.lower() == "stock":

            if side.lower() == "buy":
                portfolio[symbol]["stock_qty"] += qty
                portfolio[symbol]["stock_cost"] += qty * price

            else:
                portfolio[symbol]["stock_qty"] -= qty

        elif asset_type.lower() == "call":

            if side.lower() == "buy":
                portfolio[symbol]["call_qty"] += qty
                portfolio[symbol]["call_cost"] += qty * price

            else:
                portfolio[symbol]["call_qty"] -= qty

        elif asset_type.lower() == "put":

            if side.lower() == "buy":
                portfolio[symbol]["put_qty"] += qty
                portfolio[symbol]["put_cost"] += qty * price

            else:
                portfolio[symbol]["put_qty"] -= qty

    return portfolio