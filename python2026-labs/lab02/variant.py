# Лабораторная работа 2. Индивидуальный вариант 10
# Общий объём — количество бутылок, вместимость — бутылок в ящике.

total_bottles = int(input("Количество бутылок: "))
bottles_per_box = int(input("Бутылок в ящике (больше 0): "))

full_boxes = total_bottles // bottles_per_box
remainder = total_bottles % bottles_per_box
boxes_needed = (total_bottles + bottles_per_box - 1) // bottles_per_box

print(f"Полностью заполненных ящиков: {full_boxes}")
print(f"Остаток бутылок: {remainder}")
print(f"Всего ящиков нужно: {boxes_needed}")
