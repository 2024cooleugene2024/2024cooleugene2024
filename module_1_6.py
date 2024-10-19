# Создаем словарь с несколькими парами ключ-значение
my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print("Initial dictionary:", my_dict)

# Вывод значения по существующему ключу
print("Value for 'Masha':", my_dict['Masha'])

# Попытка получить значение по несуществующему ключу с использованием метода get()
print("Value for 'Ivan' (non-existing):", my_dict.get('Ivan', None))

# Добавляем две новые пары ключ-значение
my_dict['Kamila'] = 1981
my_dict['Artem'] = 1915
print("Dictionary after adding new pairs:", my_dict)

# Удаляем пару по ключу и выводим значение удаленного ключа
deleted_value = my_dict.pop('Egor')
print("Deleted value for 'Egor':", deleted_value)

# Выводим итоговый словарь
print("Modified dictionary:", my_dict)

# Создаем множество с повторяющимися значениями
my_set = {1, 'Яблоко', 42.314, 'Яблоко', 1}
print("Initial set (unique values):", my_set)

# Добавляем два новых элемента в множество
my_set.add(13)
my_set.add((5, 6, 1.6))
print("Set after adding new elements:", my_set)

# Удаляем один элемент из множества
my_set.remove(1)
print("Modified set after removal:", my_set)
