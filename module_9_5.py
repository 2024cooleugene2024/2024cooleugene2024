# Класс пользовательского исключения, наследующийся от ValueError
class StepValueError(ValueError):
    pass


# Класс итератора с заданными свойствами
class Iterator:
    def __init__(self, start, stop, step=1):
        """
        Инициализация объекта итератора.

        Аргументы:
        start -- начальное значение итерации (int).
        stop -- конечное значение итерации (int).
        step -- шаг итерации (int, по умолчанию 1).

        Исключения:
        Выбрасывает StepValueError, если step равен 0.
        """
        if step == 0:
            raise StepValueError("шаг не может быть равен 0")
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start  # Инициализация указателя на начальное значение

    def __iter__(self):
        """
        Метод __iter__ для инициализации итерации.

        Сбрасывает указатель pointer на значение start и возвращает объект итератора.
        """
        self.pointer = self.start  # Сбрасываем указатель
        return self

    def __next__(self):
        """
        Метод __next__ для итерации.

        Увеличивает значение указателя pointer на step и возвращает текущее значение pointer.
        Итерация завершается, когда pointer выходит за границы диапазона (start, stop)
        в зависимости от знака step.

        Исключения:
        Выбрасывает StopIteration, когда итерация завершается.
        """
        if (self.step > 0 and self.pointer >= self.stop) or (self.step < 0 and self.pointer <= self.stop):
            raise StopIteration

        current = self.pointer  # Сохраняем текущее значение указателя
        self.pointer += self.step  # Увеличиваем указатель на значение шага
        return current


# Примеры использования класса Iterator с различными конфигурациями
try:
    iter1 = Iterator(100, 200, 0)  # Создание итератора с шагом 0 для проверки исключения
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')  # Сообщение об ошибке при неверном значении шага

# Создание различных объектов итератора для тестирования
iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

# Вывод значений каждого итератора на консоль
for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()
