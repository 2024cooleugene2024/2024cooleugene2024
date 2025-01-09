import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect("not_telegram.db")
cursor = conn.cursor()

# Создаём таблицу Users, если она ещё не существует
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
);
""")
conn.commit()

# Заполняем таблицу 10 записями
users = [
    ("User1", "example1@gmail.com", 10, 1000),
    ("User2", "example2@gmail.com", 20, 1000),
    ("User3", "example3@gmail.com", 30, 1000),
    ("User4", "example4@gmail.com", 40, 1000),
    ("User5", "example5@gmail.com", 50, 1000),
    ("User6", "example6@gmail.com", 60, 1000),
    ("User7", "example7@gmail.com", 70, 1000),
    ("User8", "example8@gmail.com", 80, 1000),
    ("User9", "example9@gmail.com", 90, 1000),
    ("User10", "example10@gmail.com", 100, 1000)
]
cursor.executemany("""
INSERT OR IGNORE INTO Users (username, email, age, balance)
VALUES (?, ?, ?, ?)
""", users)
conn.commit()

# Обновляем balance у каждой 2-й записи (начиная с 1-й) на 500
cursor.execute("""
UPDATE Users SET balance = 500 WHERE id % 2 = 1
""")
conn.commit()

# Удаляем каждую 3-ю запись, начиная с 1-й
cursor.execute("""
DELETE FROM Users WHERE id % 3 = 0
""")
conn.commit()

# Удаляем запись с id = 6
cursor.execute("""
DELETE FROM Users WHERE id = 6
""")
conn.commit()

# Считаем общее количество пользователей
cursor.execute("""
SELECT COUNT(*) FROM Users
""")
total_users = cursor.fetchone()[0]

# Считаем сумму всех балансов
cursor.execute("""
SELECT SUM(balance) FROM Users
""")
all_balances = cursor.fetchone()[0]

# Выводим средний баланс
if total_users > 0:
    average_balance = all_balances / total_users
    print(f"Средний баланс пользователей: {average_balance:.2f}")
else:
    print("Нет данных для расчёта среднего баланса.")

# Закрываем соединение с базой данных
conn.close()
