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

    return rows
