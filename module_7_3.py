import string


class WordsFinder:
    def __init__(self, *file_names):
        # Сохраняем переданные имена файлов в атрибут в виде списка
        self.file_names = list(file_names)

    def get_all_words(self):
        # Создаем пустой словарь для хранения слов из файлов
        all_words = {}

        # Перебираем каждый файл и обрабатываем его содержимое
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()  # Приводим текст к нижнему регистру

                # Убираем пунктуацию
                for punctuation in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(punctuation, '')

                # Разбиваем текст на слова
                words = text.split()

                # Записываем список слов в словарь
                all_words[file_name] = words

        return all_words

    def find(self, word):
        # Получаем все слова из файлов
        all_words = self.get_all_words()

        # Создаем словарь для хранения позиций
        positions = {}

        # Ищем позицию первого вхождения слова в каждом файле
        for file_name, words in all_words.items():
            try:
                index = words.index(word.lower()) + 1  # Индексация начинается с 1
                positions[file_name] = index
            except ValueError:
                # Если слово не найдено
                positions[file_name] = None

        return positions

    def count(self, word):
        # Получаем все слова из файлов
        all_words = self.get_all_words()

        # Создаем словарь для хранения количества вхождений
        counts = {}

        # Подсчитываем количество вхождений слова в каждом файле
        for file_name, words in all_words.items():
            count = words.count(word.lower())
            counts[file_name] = count

        return counts


# Создаем объект с файлом 'test_file.txt'
finder2 = WordsFinder('test_file.txt')

# Выводим все слова из файла
print(finder2.get_all_words())  # Все слова

# Ищем первое вхождение слова 'TEXT'
print(finder2.find('TEXT'))  # 3 слово по счёту

# Подсчитываем количество вхождений слова 'teXT'
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
