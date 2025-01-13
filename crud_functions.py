import sqlite3

DB_PATH = "products.db"  # Ensure this matches the database file path in your bot script


def initiate_db():
    """Creates the Products and Users tables if they do not exist."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                price INTEGER NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL,
                age INTEGER NOT NULL,
                balance INTEGER NOT NULL DEFAULT 1000
            )
        """)
        conn.commit()


def add_user(username, email, age):
    """Adds a new user to the Users table with the default balance of 1000."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Users (username, email, age, balance)
            VALUES (?, ?, ?, ?)
        """, (username, email, age, 1000))
        conn.commit()


def is_included(username):
    """Returns True if a user with the given username exists in the Users table."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM Users WHERE username = ?", (username,))
        return cursor.fetchone() is not None


def get_all_products():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        return cursor.fetchall()
    products = [
        ("Product1", "Description1", 100),
        ("Product2", "Description2", 200),
        ("Product3", "Description3", 300),
        ("Product4", "Description4", 400),
    ]
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", products)
        conn.commit()
    print("Products table populated successfully.")


if __name__ == "__main__":
    initiate_db()
