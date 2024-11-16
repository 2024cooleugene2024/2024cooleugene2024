def all_variants(text):
    """
    Генератор возвращает подпоследовательности строки text.

    :param text: Исходная строка:
    yield: Подпоследовательность строки
    """
    # Внешний цикл перебирает начальные индексы
    for start in range(len(text)):
        # Внутренний цикл перебирает конечные индексы
        for end in range(start + 1, len(text) + 1):
            yield text[start:end]


# Пример использования
if __name__ == "__main__":
    a = all_variants("abc")
    for i in a:
        print(i)
