# Дано
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# 1. Генераторная сборка для разницы длин строк из списков first и second, если их длины не равны
first_result = (
    abs(len(f) - len(s))
    for f, s in zip(first, second)
    if len(f) != len(s)
)

# 2. Генераторная сборка для сравнения длин строк из списков first и second (без zip)
second_result = (
    len(first[i]) == len(second[i])
    for i in range(min(len(first), len(second)))
)

# Вывод результатов в виде списков для удобного просмотра
print(list(first_result))   # Ожидается: [1, 2]
print(list(second_result))  # Ожидается: [False, False, True]
