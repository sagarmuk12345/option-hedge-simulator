import sqlite3
from datetime import datetime


def save_price(symbol, price):

    conn = sqlite3.connect("database/trades.db")

    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO current_prices
        (
            symbol,
            price,
            last_updated
        )
        VALUES (?, ?, ?)
    """,
    (
        symbol.upper(),
        price,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()

    conn.close()


def get_price(symbol):

    conn = sqlite3.connect("database/trades.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            price
        FROM current_prices
        WHERE symbol = ?
    """,
    (
        symbol.upper(),
    ))

    row = cursor.fetchone()

    conn.close()

    if row:
        return row[0]

    return None


def get_all_prices():

    conn = sqlite3.connect("database/trades.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            symbol,
            price,
            last_updated
        FROM current_prices
        ORDER BY symbol
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows