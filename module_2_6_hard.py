def find_valid_pairs(n):
    result = ""

    # Перебор всех возможных уникальных пар чисел от 1 до 20
    for i in range(1, 21):
        for j in range(i + 1, 21):
            pair_sum = i + j

            # Проверка кратности
            if pair_sum > 0 and n % pair_sum == 0:
                result += f"{i}{j}"

    return result


# Пример использования
n = int(input("Введите число (от 3 до 20): "))

# Убедитесь, что число `n` находится в допустимом диапазоне
if 3 <= n <= 20:
    print(find_valid_pairs(n))
else:
    print("Число должно быть от 3 до 20.")
