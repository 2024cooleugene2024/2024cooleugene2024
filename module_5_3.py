class House:
    """
    Класс House:

    Класс, представляющий дом с заданным количеством этажей и методами для сравнения и арифметики.

    Методы:
        __init__(name, number_of_floors):
            Инициализирует дом с именем и количеством этажей.

        go_to(new_floor):
            Выводит номера этажей, начиная с первого этажа и до указанного этажа включительно.
            Обрабатывает случаи неправильного ввода этажа.

        __len__():
            Возвращает количество этажей дома.

        __str__():
            Возвращает строку с названием дома и количеством этажей.

        __eq__(self, other):
            Сравнивает количество этажей двух домов.

        __lt__(self, other):
            Проверяет, меньше ли количество этажей у self по сравнению с other.

        __le__(self, other):
            Проверяет, меньше или равно ли количество этажей у self по сравнению с other.

        __gt__(self, other):
            Проверяет, больше ли количество этажей у self по сравнению с other.

        __ge__(self, other):
            Проверяет, больше или равно ли количество этажей у self по сравнению с other.

        __ne__(self, other):
            Проверяет, неравно ли количество этажей у self по сравнению с other.

        __add__(self, value):
            Увеличивает количество этажей на переданное значение value, возвращает self.

        __radd__(self, value):
            Работает как __add__.

        __iadd__(self, value):
            Работает как __add__.
    """

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    # Методы сравнения
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return False

    # Методы для работы с арифметикой
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


# Пример использования
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __eq__
print(h1 == h2)

# __add__
h1 += 10
print(h1)
print(h1 == h2)

# __iadd__
h1 += 10
print(h1)

# __radd__
h2 = 10 + h2
print(h2)

# Сравнение этажей
print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)
