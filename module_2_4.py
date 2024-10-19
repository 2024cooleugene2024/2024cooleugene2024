# Исходный список
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Инициализация пустых списков
primes = []
not_primes = []

# Перебор списка numbers
for num in numbers:
    if num <= 1:
        continue  # Число 1 не является ни простым, ни составным

    is_prime = True  # Предполагаем, что число простое

    # Проверка на простоту числа
    for i in range(2, int(num ** 0.5) + 1):  # Проверка до квадратного корня числа
        if num % i == 0:
            is_prime = False
            break  # Если найден делитель, число не простое, выходим из цикла

    # Добавление числа в соответствующий список
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

# Вывод результатов
print("Primes:", primes)
print("Not Primes:", not_primes)
