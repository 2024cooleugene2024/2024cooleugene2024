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


# Пример использования
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)