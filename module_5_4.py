class House:
    """
    Класс House с историей строительства.

    Атрибуты класса:
        houses_history: список, хранящий названия созданных домов.

    Методы:
        __new__(cls, *args, **kwargs):
            Добавляет название дома в историю перед его созданием.

        __init__(name, number_of_floors):
            Инициализирует дом с именем и количеством этажей.

        go_to(new_floor):
            Выводит номера этажей до указанного этажа включительно.

        __del__(self):
            Уведомляет о сносе дома и выводит сообщение.

        Другие методы: __len__, __str__, перегруженные операторы (сравнение, арифметика).
    """

    houses_history = []  # Атрибут класса для хранения истории

    def __new__(cls, *args, **kwargs):
        # Добавляем название дома в историю
        instance = super().__new__(cls)
        if len(args) > 0:  # Проверяем, что есть хотя бы один аргумент
            cls.houses_history.append(args[0])  # Название дома
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        # Сообщение при удалении объекта
        print(f"{self.name} снесён, но он останется в истории")

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
        return isinstance(other, House) and self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return isinstance(other, House) and self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return isinstance(other, House) and self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return isinstance(other, House) and self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return isinstance(other, House) and self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return isinstance(other, House) and self.number_of_floors != other.number_of_floors

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
print(House.houses_history)  # ['ЖК Эльбрус']

h2 = House('ЖК Акация', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация']

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление объектов
del h2  # ЖК Акация снесён, но он останется в истории
del h3  # ЖК Матрёшки снесён, но он останется в истории

print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
