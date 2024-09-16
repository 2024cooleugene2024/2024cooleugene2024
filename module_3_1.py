calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()  # Увеличиваем счётчик вызовов
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return length, upper_case, lower_case


def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счётчик вызовов
    return string.lower() in (item.lower() for item in list_to_search)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('cube', ['recycling', 'cyclic', 'sphere']))  # No matches
print(is_contains('GaZEL', ['List', 'Snow', 'Gazelist', 'gAzeL']))  # Urban ~ urBAN

print(calls)