def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            result += item  # Пытаемся сложить только числовые значения
        except TypeError:
            print(f"Некорректный тип данных для подсчёта суммы - {item}")
            incorrect_data += 1  # Увеличиваем счётчик при ошибке типа

    return result, incorrect_data

def calculate_average(numbers):
    try:
        # Проверяем, является ли numbers коллекцией
        total_sum, incorrect_data = personal_sum(numbers)
        # Количество корректных данных = общая длина - некорректные
        correct_count = len(numbers) - incorrect_data

        # Обработка деления на 0 при пустом списке корректных данных
        return total_sum / correct_count if correct_count > 0 else 0
    except TypeError:
        # Если numbers не коллекция, выводим сообщение
        print("В numbers записан некорректный тип данных")
        return None

# Примеры использования функции
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Некорректные символы в строке
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передан не список
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Корректные данные
