# Глобальная переменная для подсчета вызовов функций
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(s):
    count_calls()  # Увеличиваем счетчик вызовов
    return (len(s), s.upper(), s.lower())

def is_contains(s, list_to_search):
    count_calls()  # Увеличиваем счетчик вызовов
    return s.lower() in (item.lower() for item in list_to_search)

# Пример вызова функций
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))    # No matches

# Вывод количества вызовов
print(calls)

