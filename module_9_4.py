# Часть 1: Лямбда-функция для сравнения символов на одинаковых позициях
first = 'Мама мыла раму'
second = 'Рамена мало было'

# Лямбда-функция для сравнения символов на одинаковых индексах
result = list(map(lambda x, y: x == y, first, second))
print("Результат сравнения символов:", result)
# Ожидаемый вывод: [False, True, True, False, False, False, False, False, True, False, False, False, False, False]

# Часть 2: Замыкание для записи данных в файл
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for data in data_set:
                file.write(str(data) + '\n')  # Преобразуем каждый элемент в строку и добавляем новую строку
    return write_everything

# Тестирование функции замыкания
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Часть 3: Функторный класс MysticBall с методом __call__
from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = list(words)  # Сохраняем слова в списке для случайного доступа

    def __call__(self):
        return choice(self.words)

# Тестирование класс-функтора MysticBall
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print("Ответ магического шара:", first_ball())
print("Ответ магического шара:", first_ball())
print("Ответ магического шара:", first_ball())
