# Вводим строку с помощью input()
my_string = input("Введите строку: ")

# Выводим количество символов в строке
print("Количество символов в строке:", len(my_string))

# Выводим строку в верхнем регистре
print("Строка в верхнем регистре:", my_string.upper())

# Выводим строку в нижнем регистре
print("Строка в нижнем регистре:", my_string.lower())

# Удаляем все пробелы из строки
my_string_no_spaces = my_string.replace(" ", "")
print("Строка без пробелов:", my_string_no_spaces)

# Выводим первый символ строки
print("Первый символ строки:", my_string[0])

# Выводим последний символ строки
print("Последний символ строки:", my_string[-1])
