def add_everything_up(a, b):
    try:
        # Попытка сложить значения
        result = a + b
    except TypeError:
        # Если типы разные, то возвращаем строковое представление
        return f"{a}{b}"
    return result

# Примеры использования функции
print(add_everything_up(123.456, 'строка'))   # Ожидаемый вывод: "123.456строка"
print(add_everything_up('яблоко', 4215))      # Ожидаемый вывод: "яблоко4215"
print(add_everything_up(123.456, 7))          # Ожидаемый вывод: 130.456
