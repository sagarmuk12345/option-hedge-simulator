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

    portfolio = {}

    for symbol, asset_type, side, quantity, price in rows:

        symbol = symbol.upper()

        if symbol not in portfolio:

            portfolio[symbol] = {
                "stock_qty": 0,
                "stock_cost": 0,

                "call_qty": 0,
                "call_cost": 0,

                "put_qty": 0,
                "put_cost": 0,

                "current_price": 0
            }

        qty = float(quantity)
        price = float(price)

        if side.lower() == "sell":
            qty = -qty

        if asset_type.lower() == "stock":

            if qty > 0:
                portfolio[symbol]["stock_cost"] += qty * price

            portfolio[symbol]["stock_qty"] += qty

    cursor.execute("""
        SELECT
            symbol,
            price
        FROM current_prices
    """)

    prices = cursor.fetchall()

    for symbol, price in prices:

        symbol = symbol.upper()

        if symbol in portfolio:
            portfolio[symbol]["current_price"] = float(price)

    conn.close()

    return portfolio