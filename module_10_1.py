from time import sleep, time
import threading

def write_words(word_count, file_name):
    with open(file_name, "w") as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # Пауза 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")

# Время начала записи
start_time = time()

# Запуск функций с аргументами
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Время окончания записи
end_time = time()
print(f'Время записи (функции): {end_time - start_time} секунд')

# Функция для выполнения в потоке
def thread_write_words(word_count, file_name):
    write_words(word_count, file_name)

# Время начала записи потоками
start_time_threads = time()

# Создание и запуск потоков
threads = []
threads.append(threading.Thread(target=thread_write_words, args=(10, 'example5.txt')))
threads.append(threading.Thread(target=thread_write_words, args=(30, 'example6.txt')))
threads.append(threading.Thread(target=thread_write_words, args=(200, 'example7.txt')))
threads.append(threading.Thread(target=thread_write_words, args=(100, 'example8.txt')))

for thread in threads:
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

# Время окончания записи потоками
end_time_threads = time()
print(f'Время записи (потоки): {end_time_threads - start_time_threads} секунд')
