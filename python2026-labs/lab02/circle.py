# Лабораторная работа 2. Дополнительное задание: окружность и круг
import math

radius = float(input("Радиус (больше 0): "))

circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f"Длина окружности: {circumference:.2f}")
print(f"Площадь круга: {area:.2f}")
