class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        """
        Создает новый экземпляр класса House и добавляет имя дома в историю.
        Аргументы:
            *args: Переменное количество аргументов. Первый аргумент должен быть именем дома.
            **kwargs: Произвольные именованные аргументы.
        Возвращает:
            House: Новый экземпляр класса House.
        """
        instance = super().__new__(cls)
        cls.houses_history.append(args[0])
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        """
        Симулирует переход на указанный этаж в доме.
        Аргументы:
            new_floor (int): Номер этажа, на который нужно перейти.
        Возвращает:
            None
        """
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for num in range(1, new_floor + 1):
                print(num)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return 'Название: ' + str(self.name) + ', кол-во этажей: ' + str(self.number_of_floors)

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        self.number_of_floors += value
        return self

    def __del__(self):
        """
        Удаляет экземпляр дома и удаляет его имя из истории, если оно присутствует.
        Возвращает:
            None
        """
        if self.name in self.houses_history:
            self.houses_history.remove(self.name)
        print(f'{self.name} снесён, но он останется в истории')