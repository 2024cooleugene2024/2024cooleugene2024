# Родительские классы
class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False  # по умолчанию растение несъедобное

# Классы-наследники для животных
class Mammal(Animal):
    def eat(self, food):
        if isinstance(food, Plant):  # проверяем, является ли пища растением
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False

class Predator(Animal):
    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False

# Классы-наследники для растений
class Flower(Plant):
    pass  # цветы остаются несъедобными по умолчанию

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # переопределяем, фрукты съедобные

# Пример использования
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
