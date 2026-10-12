# Лабораторная работа 1. Индивидуальный вариант 10
# Заказ: «Пекарня». Первая позиция — булочки, вторая — пироги.

order_name = input("Название заказа: ")
customer_name = input("Имя заказчика: ")

first_item_name = input("Первая позиция (булочки), название: ")
first_item_count = int(input("Количество, шт.: "))
first_item_price = float(input("Цена единицы, руб.: "))

second_item_name = input("Вторая позиция (пироги), название: ")
second_item_count = int(input("Количество, шт.: "))
second_item_price = float(input("Цена единицы, руб.: "))

delivery_cost = float(input("Стоимость доставки, руб.: "))
paid = float(input("Внесённая сумма, руб.: "))

first_item_cost = first_item_count * first_item_price
second_item_cost = second_item_count * second_item_price
goods_cost = first_item_cost + second_item_cost
total_cost = goods_cost + delivery_cost
total_count = first_item_count + second_item_count
change = paid - total_cost

print()
print(f"========== Заказ: {order_name} ==========")
print(f"Заказчик: {customer_name}")
print("Название", "Количество", "Цена", "Стоимость", sep=" | ")
print(first_item_name, first_item_count, f"{first_item_price:.2f}",
      f"{first_item_cost:.2f}", sep=" | ")
print(second_item_name, second_item_count, f"{second_item_price:.2f}",
      f"{second_item_cost:.2f}", sep=" | ")
print(f"Стоимость товаров без доставки: {goods_cost:.2f} руб.")
print(f"Доставка: {delivery_cost:.2f} руб.")
print(f"Итого с доставкой: {total_cost:.2f} руб.")
print(f"Всего единиц: {total_count}")
print(f"Внесено: {paid:.2f} руб.")
print(f"Сдача: {change:.2f} руб.")
