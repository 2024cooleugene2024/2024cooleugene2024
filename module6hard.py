import math
from typing import List, Tuple


class Figure:
    sides_count: int = 0

    def __init__(self, color: Tuple[int, int, int], *sides: int) -> None:
        """
        Инициализация объекта класса Figure.

        :param color: Кортеж значений RGB (r, g, b) в диапазоне от 0 до 255.
        :param sides: Список сторон фигуры. Количество сторон зависит от типа фигуры.
        """
        self.__color: List[int] = list(color) if self.__is_valid_color(*color) else [0, 0, 0]
        self.__sides: List[int] = list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count
        self.filled: bool = False

    def get_color(self) -> List[int]:
        """
        Возвращает цвет фигуры в формате RGB.

        :return: Список из трёх чисел, представляющих цвет в формате RGB.
        """
        return self.__color

    def __is_valid_color(self, r: int, g: int, b: int) -> bool:
        """
        Проверяет корректность переданного цвета.

        :param r: Значение красного компонента (0-255).
        :param g: Значение зелёного компонента (0-255).
        :param b: Значение синего компонента (0-255).
        :return: True, если значения корректны, иначе False.
        """
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r: int, g: int, b: int) -> None:
        """
        Устанавливает цвет фигуры, если переданы корректные значения.

        :param r: Значение красного компонента (0-255).
        :param g: Значение зелёного компонента (0-255).
        :param b: Значение синего компонента (0-255).
        """
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides: int) -> bool:
        """
        Проверяет корректность переданных сторон фигуры.

        :param new_sides: Новые стороны фигуры.
        :return: True, если все стороны положительные целые числа и их количество равно sides_count, иначе False.
        """
        return (len(new_sides) == self.sides_count and
                all(isinstance(side, int) and side > 0 for side in new_sides))

    def get_sides(self) -> List[int]:
        """
        Возвращает текущие стороны фигуры.

        :return: Список сторон.
        """
        return self.__sides

    def set_sides(self, *new_sides: int) -> None:
        """
        Устанавливает новые стороны фигуры, если их количество и значения корректны.

        :param new_sides: Новые значения сторон.
        """
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self) -> int:
        """
        Возвращает периметр фигуры, который является суммой всех сторон.

        :return: Периметр (сумма сторон).
        """
        return sum(self.__sides)


class Circle(Figure):
    sides_count: int = 1

    def __init__(self, color: Tuple[int, int, int], *sides: int) -> None:
        """
        Инициализация объекта класса Circle.

        :param color: Кортеж значений RGB (r, g, b).
        :param sides: Длина окружности.
        """
        super().__init__(color, *sides)
        self.__radius: float = self.get_sides()[0] / (2 * math.pi)

    def get_square(self) -> float:
        """
        Возвращает площадь круга.

        :return: Площадь круга.
        """
        return math.pi * (self.__radius ** 2)

    def __len__(self) -> int:
        """
        Возвращает длину окружности, которая является периметром.

        :return: Длина окружности.
        """
        return self.get_sides()[0]


class Triangle(Figure):
    sides_count: int = 3

    def get_square(self) -> float:
        """
        Возвращает площадь треугольника, используя формулу Герона.

        :return: Площадь треугольника.
        """
        a, b, c = self.get_sides()
        s = sum([a, b, c]) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count: int = 12

    def __init__(self, color: Tuple[int, int, int], *sides: int) -> None:
        """
        Инициализация объекта класса Cube.

        :param color: Кортеж значений RGB (r, g, b).
        :param sides: Длина одного ребра куба.
        """
        super().__init__(color, *([sides[0]] * self.sides_count) if len(sides) == 1 else sides)

    def get_volume(self) -> int:
        """
        Возвращает объём куба.

        :return: Объём куба.
        """
        edge = self.get_sides()[0]
        return edge ** 3


# Тестирование

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())  # [55, 66, 77]
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())  # [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())  # [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1))  # 15

# Проверка объёма (куба):
print(cube1.get_volume())  # 216
