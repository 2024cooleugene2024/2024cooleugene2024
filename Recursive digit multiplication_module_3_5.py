def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Если длина строки равна 1, возвращаем это число как результат
    if len(str_number) == 1:
        return int(str_number)

    # Первая цифра числа
    first = int(str_number[0])

    # Если первая цифра 0, просто пропускаем её и продолжаем работу с оставшейся частью числа
    if first == 0:
        return get_multiplied_digits(int(str_number[1:]))

    # Рекурсивно умножаем первую цифру на результат функции для оставшейся части числа
    return first * get_multiplied_digits(int(str_number[1:]))


# Пример использования
result = get_multiplied_digits(40203)
print(result)
