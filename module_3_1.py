calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    line = str(string)
    result = (len(line), line.upper(), line.lower())
    count_calls()
    return result


def is_contains(string, list_to_search):
    global result
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('cube', ['recycling', 'cyclic', 'sphere']))  # No matches
print(is_contains('GaZEL', ['List', 'Snow', 'Gazelist', 'gAzeL']))  # Urban ~ urBAN

print(calls)
