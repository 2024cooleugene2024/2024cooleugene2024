class Runner:
    def __init__(self, name, speed=5):
        # Проверка, что имя является строкой
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')

        # Проверка, что скорость положительная
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

        self.distance = 0

    def run(self):
        """Бег на двойной скорости."""
        self.distance += self.speed * 2

    def walk(self):
        """Ходьба на базовой скорости."""
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        """Сравнение бегунов по имени."""
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name
        return False
