# Лабораторная работа 4. Индивидуальный вариант 10
# Условие отбора: числа не меньше 10. Весь ввод в списке не хранится.

THRESHOLD = 10

n = int(input("Количество чисел n (не меньше 0): "))

count = 0
total = 0

for index in range(n):
    number = int(input(f"Число {index + 1}: "))
    if number >= THRESHOLD:
        count += 1
        total += number

print(f"Количество чисел не меньше {THRESHOLD}: {count}")
print(f"Сумма таких чисел: {total}")
