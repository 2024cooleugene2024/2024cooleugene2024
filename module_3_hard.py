def calculate_structure_sum(data):
    """
    :param data:
    :return:
    """
    total_sum = 0

    # Рекурсивная функция для обхода элементов
    def recursive_sum(item):
        """
        :param item:
        """
        nonlocal total_sum

        if isinstance(item, int):  # Если элемент - число, добавляем его к сумме
            total_sum += item
        elif isinstance(item, str):  # Если элемент - строка, добавляем её длину
            total_sum += len(item)
        elif isinstance(item, (list, tuple, set)):  # Если это список, кортеж или множество, проходим по каждому элементу
            for elem in item:
                recursive_sum(elem)
        elif isinstance(item, dict):  # Если это словарь, проходим по ключам и значениям
            for key, value in item.items():
                recursive_sum(key)
                recursive_sum(value)

    # Запускаем рекурсивную обработку переданного объекта
    recursive_sum(data)

    return total_sum

# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
