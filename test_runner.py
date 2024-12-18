# test_runner.py
import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        # Создаем объект класса Runner
        runner = Runner("TestRunner")
        # Вызываем метод walk 10 раз
        for _ in range(10):
            runner.walk()
        # Проверяем, что дистанция равна 50
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        # Создаем объект класса Runner
        runner = Runner("TestRunner")
        # Вызываем метод run 10 раз
        for _ in range(10):
            runner.run()
        # Проверяем, что дистанция равна 100
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        # Создаем два объекта класса Runner
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        # Вызываем метод run 10 раз для первого объекта
        for _ in range(10):
            runner1.run()
        # Вызываем метод walk 10 раз для второго объекта
        for _ in range(10):
            runner2.walk()
        # Проверяем, что дистанции различны
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == "__main__":
    unittest.main()
