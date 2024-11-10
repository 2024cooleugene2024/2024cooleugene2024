# Заданные списки строк
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1. Создание списка длин строк из first_strings, если длина строки не менее 5 символов
first_result = [len(word) for word in first_strings if len(word) >= 5]

# 2. Создание списка пар слов одинаковой длины из двух списков (два цикла)
second_result = [
    (first_word, second_word)
    for first_word in first_strings
    for second_word in second_strings
    if len(first_word) == len(second_word)
]

# 3. Создание словаря из объединённых списков, где ключ - строка, значение - длина строки,
# и только для строк с чётной длиной
third_result = {
    word: len(word)
    for word in first_strings + second_strings
    if len(word) % 2 == 0
}

# Вывод результатов
print(first_result)
print(second_result)
print(third_result)
