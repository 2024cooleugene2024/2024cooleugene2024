# file: introspection_tool.py

def introspection_info(obj):
    """
    Функция проводит интроспекцию объекта и возвращает подробную информацию о нём.
    :param obj: Любой объект для анализа.
    :return: Словарь с информацией об объекте.
    """
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты и методы объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]

    # Определяем модуль, к которому принадлежит объект
    obj_module = getattr(obj, '__module__', 'Built-in or Unknown')

    # Интересные свойства объекта
    docstring = getattr(obj, '__doc__', 'No documentation available')

    # Возвращаем собранные данные
    return {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
        'docstring': docstring
    }

# Пример использования
if __name__ == '__main__':
    # Пример с числом
    number_info = introspection_info(42)
    print("Introspection of int:")
    print(number_info)

    # Пример с пользовательским классом
    class MyClass:
        """Это пример пользовательского класса для интроспекции."""
        def __init__(self, value):
            self.value = value

        def my_method(self):
            return f"Value is {self.value}"

    my_obj = MyClass(10)
    my_obj_info = introspection_info(my_obj)
    print("\nIntrospection of MyClass:")
    print(my_obj_info)
