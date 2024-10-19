def get_matrix(n, m, value):
    # Создаем пустой список для матрицы
    matrix = []

    # Внешний цикл для строк
    for _ in range(n):
        # Создаем пустой список для строки
        row = []
        # Внутренний цикл для столбцов
        for _ in range(m):
            # Заполняем строку значением value
            row.append(value)
        # Добавляем заполненную строку в матрицу
        matrix.append(row)

    # Возвращаем готовую матрицу
    return matrix


# Примеры использования функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Выводим результаты
print(result1)
print(result2)
print(result3)
