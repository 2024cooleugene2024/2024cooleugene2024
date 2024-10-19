def single_root_words(root_word, *other_words):
    same_words = []  # Создаем пустой список для подходящих слов
    root_word_lower = root_word.lower()  # Преобразуем корневое слово в нижний регистр

    # Перебираем остальные слова
    for word in other_words:
        word_lower = word.lower()  # Преобразуем текущее слово в нижний регистр
        # Проверяем, содержится ли корневое слово в текущем слове или наоборот
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)  # Добавляем подходящее слово в список

    return same_words  # Возвращаем список подходящих слов


# Пример вызова функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Выводим результаты
print(result1)  # ['richiest', 'orichalcum', 'richies']
print(result2)  # ['Able', 'Disable']
