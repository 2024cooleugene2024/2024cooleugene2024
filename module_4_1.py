# module_4_1.py

from fake_math import divide as fake_divide
from true_math import divide as true_divide

# Примеры вызовов функций
result1 = fake_divide(69, 3)  # Ожидаемый результат: 23.0
result2 = fake_divide(3, 0)  # Ожидаемый результат: 'Ошибка'
result3 = true_divide(49, 7)  # Ожидаемый результат: 7.0
result4 = true_divide(15, 0)  # Ожидаемый результат: inf

# Вывод результатов на экран
print(result1)  # 23.0
print(result2)  # Ошибка
print(result3)  # 7.0
print(result4)  # inf
