# Лабораторная работа 4. Задание 1: диапазон в обе стороны

a = int(input("a: "))
b = int(input("b: "))

if a <= b:
    # range не включает stop, поэтому берём b + 1
    for number in range(a, b + 1):
        print(number)
else:
    # по убыванию: шаг -1, stop = b - 1, чтобы b вошло в вывод
    for number in range(a, b - 1, -1):
        print(number)
