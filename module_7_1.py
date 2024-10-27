class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                products = file.read()
            return products
        except FileNotFoundError:
            return ''

    def add(self, *products):
        existing_products = self.get_products()
        existing_names = [line.split(', ')[0] for line in existing_products.strip().split('\n') if line]
        for product in products:
            if product.name not in existing_names:
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')
            else:
                print(f'Продукт {product} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # Выводит: Spaghetti, 3.4, Groceries

s1.add(p1, p2, p3)

print(s1.get_products())
