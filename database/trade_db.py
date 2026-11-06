import sqlite3


def save_trade(
    symbol,
    asset_type,
    side,
    quantity,
    price,
    strike,
    expiry
):

    conn = sqlite3.connect("database/trades.db")

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO trades
        (
            symbol,
            asset_type,
            side,
            quantity,
            price,
            strike,
            expiry
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    (
        symbol,
        asset_type,
        side,
        quantity,
        price,
        strike,
        expiry
    ))

    conn.commit()
    conn.close()


def get_all_trades():

    conn = sqlite3.connect("database/trades.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            symbol,
            asset_type,
            side,
            quantity,
            price,
            strike,
            expiry
        FROM trades
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows