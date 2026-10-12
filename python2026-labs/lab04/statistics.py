# Лабораторная работа 4. Задание 2: статистика потока (без списка)

n = int(input("Количество чисел n (не меньше 1): "))

total = 0
positive_count = 0
maximum = 0

for index in range(n):
    number = int(input(f"Число {index + 1}: "))
    total += number
    if number > 0:
        positive_count += 1
    # максимум инициализируем первым введённым значением
    if index == 0 or number > maximum:
        maximum = number

print(f"Сумма: {total}")
print(f"Положительных: {positive_count}")
print(f"Максимум: {maximum}")
