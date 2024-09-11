numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # исходный список
n = 0
primes = []
not_primes = []
i = 0
for i in range(len(numbers)):
    is_prime = True
    n = numbers[i]
    if n < 2:
        print(n, '- не простое число и не сложное число также!')
        continue
    else:
        f = n ** (1 / 2)
    for a in range(2, int(f + 1)):
        if n % a == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(n)
    else:
        not_primes.append(n)
is_prime = True  # признак простого числа
print('Вот они простые числа ', primes)
print('А вот тут составные числа', not_primes)
