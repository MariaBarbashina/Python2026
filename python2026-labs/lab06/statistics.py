# Лабораторная работа 6. Задание 1: статистика списка

numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))

if len(numbers) == 0:
    print("Нет данных")
else:
    count = len(numbers)
    total = sum(numbers)
    average = total / count
    print(f"Количество: {count}")
    print(f"Сумма: {total}")
    print(f"Минимум: {min(numbers)}")
    print(f"Максимум: {max(numbers)}")
    print(f"Среднее: {average:.2f}")
