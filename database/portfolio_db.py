import sqlite3


def get_portfolio():

    conn = sqlite3.connect("database/trades.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            symbol,
            asset_type,
            side,
            quantity
        FROM trades
    """)

    rows = cursor.fetchall()

    conn.close()

    portfolio = {}

    for symbol, asset_type, side, quantity in rows:

        if symbol not in portfolio:

            portfolio[symbol] = {
                "stock": 0,
                "call": 0,
                "put": 0
            }

        qty = float(quantity)

        if side.lower() == "sell":
            qty = -qty

        if asset_type.lower() == "stock":
            portfolio[symbol]["stock"] += qty

        elif asset_type.lower() == "call":
            portfolio[symbol]["call"] += qty

        elif asset_type.lower() == "put":
            portfolio[symbol]["put"] += qty

    return portfolio