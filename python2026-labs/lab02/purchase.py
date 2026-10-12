# Лабораторная работа 2. Задание 2: стоимость покупки

price = int(input("Цена одной тетради, руб.: "))
count = int(input("Количество тетрадей: "))
paid = int(input("Переданная сумма, руб.: "))

cost = price * count
change = paid - cost

print(f"Стоимость: {cost}")
print(f"Сдача: {change}")
