# Исходные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразуем множество студентов в отсортированный список
students_sorted = sorted(students)

# Создаем пустой словарь для хранения среднего балла
average_grades = {}

# Используем zip для соединения студентов с их оценками
for student, grade in zip(students_sorted, grades):
    average_grade = sum(grade) / len(grade)
    average_grades[student] = average_grade

# Выводим словарь со средними баллами
print(average_grades)
