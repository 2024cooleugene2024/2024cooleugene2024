import os
import time

# Укажите путь к каталогу, в котором хотите выполнить обход
directory = "."

# Обход каталога с помощью os.walk
for root, dirs, files in os.walk(directory):
    for file in files:
        # Полный путь к файлу
        filepath = os.path.join(root, file)

        # Время последнего изменения файла
        filetime = os.path.getmtime(filepath)

        # Форматированное время последнего изменения
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Размер файла в байтах
        filesize = os.path.getsize(filepath)

        # Родительская директория файла
        parent_dir = os.path.dirname(filepath)

        # Вывод информации о файле
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
            f' Родительская директория: {parent_dir}')
