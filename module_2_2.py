first = int(input('Введите первое число '))
print("Введено значение", first)

second = int(input('Введите второе число '))
print("Введено значение", second)

third = int(input('Введите третье число '))
print('Введено значение', third)

if first == second and second == third and first == third:
    print('3')
elif first == second or second == third or first == third:
    print('2')
else:
    print('0')
