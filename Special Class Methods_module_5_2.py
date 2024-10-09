class House:
    """
    Класс House:

    Класс, представляющий дом с заданным количеством этажей и методом для перехода на новый этаж.

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


# Пример использования
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
