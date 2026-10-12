# Лабораторная работа 6. Задание 2: независимое преобразование
# Новый список: отрицательные числа заменены модулями. Исходный не меняется.

numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))

transformed = []
for number in numbers:
    if number < 0:
        transformed.append(-number)
    else:
        transformed.append(number)

print(f"Исходный список: {numbers}")
print(f"Новый список: {transformed}")
