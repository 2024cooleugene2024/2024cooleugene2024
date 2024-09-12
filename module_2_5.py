def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix
n = int(input('Введите количество строк матрицы: '))
m = int(input('Введите количество столбцов матрицы: '))
value = input(f'Введите значения матрицы: ')
print('-------' * m)
matrix = get_matrix(n, m, value)

# Исходный код: Вводим в консоль
# result1 = get_matrix(2, 2, 10)
# result2 = get_matrix(3, 5, 42)
# result3 = get_matrix(4, 2, 13)
# print(result1)
# print(result2)
# print(result3)