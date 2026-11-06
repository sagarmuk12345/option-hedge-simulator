import sqlite3

conn = sqlite3.connect("database/trades.db")

cursor = conn.cursor()

# Trades Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS trades
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    symbol TEXT,

    asset_type TEXT,

    side TEXT,

    quantity REAL,

    price REAL,

    strike REAL,

    expiry TEXT
)
""")

# Current Prices Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS current_prices
(
    symbol TEXT PRIMARY KEY,

    price REAL,

    last_updated TEXT
)
""")

conn.commit()

conn.close()

print("Database created successfully")