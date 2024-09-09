immutable_var = 1, 2, 3, 4, True, "string"
print(immutable_var)

immutable_var[0] = 200  # Кортеж не поддерживает обращение по элементам
print(immutable_var)

mutable_list = [1, 2, "melon", "peach"]
print(mutable_list)
mutable_list[2] = "banana"
print(mutable_list)
