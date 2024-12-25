import unittest


def skip_if_frozen(test_func):
    """Декоратор для пропуска тестов, если is_frozen = True."""
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        return test_func(self, *args, **kwargs)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False  # Атрибут управления заморозкой тестов

    @skip_if_frozen
    def test_challenge(self):
        self.assertEqual(1 + 1, 2)

    @skip_if_frozen
    def test_run(self):
        self.assertTrue("runner".startswith("run"))

    @skip_if_frozen
    def test_walk(self):
        self.assertIn("walk", ["run", "walk", "jump"])


class TournamentTest(unittest.TestCase):
    is_frozen = True  # Атрибут управления заморозкой тестов

    @skip_if_frozen
    def test_first_tournament(self):
        self.assertEqual(len([1, 2, 3]), 3)

    @skip_if_frozen
    def test_second_tournament(self):
        self.assertGreater(5, 2)

    @skip_if_frozen
    def test_third_tournament(self):
        self.assertNotEqual(10, 0)
