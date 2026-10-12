# Лабораторная работа 3. Задание 1: минимум трёх чисел
# Функции min, max и сортировка не используются.

first = int(input("Первое число: "))
second = int(input("Второе число: "))
third = int(input("Третье число: "))

if first <= second and first <= third:
    minimum = first
elif second <= third:
    minimum = second
else:
    minimum = third

print(f"Минимум: {minimum}")
