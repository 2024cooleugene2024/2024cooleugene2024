import os
import time
from multiprocessing import Pool

# Функция для чтения информации из файла
def read_info(name):
    all_data = []  # Локальный список для хранения данных
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:  # Если строка пустая, прерываем цикл
                break
            all_data.append(line)
    # В данной задаче возвращать или выводить список не требуется

# Список названий файлов
filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный подход
def linear_read(filenames):
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print(f"Линейный вызов: {end_time - start_time:.6f} секунд")

# Многопроцессный подход
def multiprocess_read(filenames):
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f"Многопроцессный вызов: {end_time - start_time:.6f} секунд")

# Основной блок программы
if __name__ == '__main__':

    # Линейное выполнение
    linear_read(filenames)

    # Многопроцессное выполнение
    multiprocess_read(filenames)