import unittest
import logging
from runner_module import Runner

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,  # Уровень логирования
    filename='runner_tests.log',  # Название файла
    filemode='w',  # Перезапись файла
    encoding='utf-8',  # Кодировка
    format='%(asctime)s - %(levelname)s - %(message)s'  # Формат сообщений
)


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """Тест метода walk с проверкой исключения для скорости."""
        try:
            # Создание бегуна с отрицательной скоростью (вызывает исключение)
            runner = Runner(name="Бегун", speed=-5)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            # Логируем предупреждение при исключении
            logging.warning("Неверная скорость для Runner: %s", str(e))

    def test_run(self):
        """Тест метода run с проверкой исключения для имени."""
        try:
            # Создание бегуна с некорректным именем (вызывает исключение)
            runner = Runner(name=12345, speed=5)
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            # Логируем предупреждение при исключении
            logging.warning("Неверный тип данных для объекта Runner: %s", str(e))


if __name__ == "__main__":
    unittest.main()
