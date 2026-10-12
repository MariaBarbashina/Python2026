# Лабораторная работа 6. Дополнительное задание: удаление повторов без set
# Порядок первого появления сохраняется.

numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))

unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(f"Исходный список: {numbers}")
print(f"Без повторов: {unique_numbers}")
