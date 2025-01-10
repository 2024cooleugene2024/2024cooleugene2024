import sqlite3

DB_PATH = "products.db"  # Ensure this matches the database file path in your bot script


def populate_products():
    """Populates the Products table with sample data."""
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
    populate_products()
