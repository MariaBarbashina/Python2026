# Лабораторная работа 6. Индивидуальный вариант 10
# Условие отбора: числа не меньше 10.

THRESHOLD = 10

numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))

selected = []
for number in numbers:
    if number >= THRESHOLD:
        selected.append(number)

sorted_selected = sorted(selected)

print(f"Исходный список: {numbers}")
print(f"Числа не меньше {THRESHOLD}: {selected}")
print(f"Количество: {len(selected)}")
print(f"Сумма: {sum(selected)}")
print(f"Отсортированная копия: {sorted_selected}")
