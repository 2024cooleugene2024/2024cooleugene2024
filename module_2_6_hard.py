def generate_password(n):
    import itertools

    # Создание строки для пар
    digits = '0123456789'
    pairs = []

    # Создаем все возможные пары
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            pairs.append(digits[i] + digits[j])

    # Список для хранения пар, которые удовлетворяют условию
    valid_pairs = []

    # Проверка условий
    for pair in pairs:
        # Получаем цифры пары
        a = int(pair[0])
        b = int(pair[1])
        pair_sum = a + b

        # Проверяем кратность
        if n % pair_sum == 0:
            valid_pairs.append(pair)

    # Формируем пароль
    password = ''.join(valid_pairs)

    return password


# Пример использования
n = 30  # Или любое другое число от 3 до 20
print(generate_password(n))
