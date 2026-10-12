# Лабораторная работа 4. Задание 3: повторный ввод

rejected_count = 0
number = int(input("Введите положительное целое число: "))

while number <= 0:
    rejected_count += 1
    print("Число не положительное, попробуйте ещё раз.")
    number = int(input("Введите положительное целое число: "))

print(f"Квадрат: {number ** 2}")
print(f"Отклонено попыток: {rejected_count}")
