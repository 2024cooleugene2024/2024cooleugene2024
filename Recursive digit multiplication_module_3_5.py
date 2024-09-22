def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Если длина строки 1 и это не '0', возвращаем эту цифру
    if len(str_number) == 1:
        return int(str_number) if str_number != '0' else 1

    # Получаем первую цифру числа
    first = int(str_number[0])

    # Если первая цифра равна 0, пропускаем ее и рекурсивно продолжаем работу с оставшимися цифрами
    if first == 0:
        return get_multiplied_digits(int(str_number[1:]))

    # Рекурсивное умножение первой цифры на произведение оставшихся цифр
    return first * get_multiplied_digits(int(str_number[1:]))


# Пример использования:
print(get_multiplied_digits(240))  # Вывод: 8
print(get_multiplied_digits(40203))  # Вывод: 24
