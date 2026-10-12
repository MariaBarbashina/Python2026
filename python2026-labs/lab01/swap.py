# Лабораторная работа 1. Задание 4: обмен значениями

first_room = input("Первая аудитория: ")
second_room = input("Вторая аудитория: ")

print("До обмена:")
print(f"first_room = {first_room}")
print(f"second_room = {second_room}")

temp_room = first_room
first_room = second_room
second_room = temp_room

print("После обмена:")
print(f"first_room = {first_room}")
print(f"second_room = {second_room}")
