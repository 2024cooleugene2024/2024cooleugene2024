# Создаем кортеж, неизменяемая переменная
immutable_var = (1, 2, 'a', 'b')
print("Immutable tuple:", immutable_var)

# Попытка изменить элементы кортежа (это вызовет ошибку)
try:
    immutable_var[0] = 100  # Это невозможно, кортежи неизменяемы
except TypeError as e:
    print("Ошибка:", e)

# Кортежи неизменяемы, поэтому изменить отдельные элементы напрямую нельзя.

# Создаем список, изменяемая переменная
mutable_list = [1, 2, 'a', 'b']
print("Original list:", mutable_list)

# Изменяем элементы списка
mutable_list[0] = 100
mutable_list.append('Modified')

# Выводим измененный список
print("Modified list:", mutable_list)
