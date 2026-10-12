# Лабораторная работа 1. Дополнительное задание
# Вариант 10 «Пекарня» со скидкой в процентах от стоимости товаров.
# Скидка не затрагивает доставку.

order_name = input("Название заказа: ")
customer_name = input("Имя заказчика: ")

first_item_name = input("Первая позиция (булочки), название: ")
first_item_count = int(input("Количество, шт.: "))
first_item_price = float(input("Цена единицы, руб.: "))

second_item_name = input("Вторая позиция (пироги), название: ")
second_item_count = int(input("Количество, шт.: "))
second_item_price = float(input("Цена единицы, руб.: "))

delivery_cost = float(input("Стоимость доставки, руб.: "))
discount_percent = float(input("Скидка на товары, % (от 0 до 100): "))
paid = float(input("Внесённая сумма, руб.: "))

first_item_cost = first_item_count * first_item_price
second_item_cost = second_item_count * second_item_price
goods_cost = first_item_cost + second_item_cost
discount_amount = goods_cost * discount_percent / 100
total_cost = goods_cost - discount_amount + delivery_cost
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
print(f"Скидка {discount_percent:.2f}%: {discount_amount:.2f} руб.")
print(f"Доставка: {delivery_cost:.2f} руб.")
print(f"Итого со скидкой и доставкой: {total_cost:.2f} руб.")
print(f"Всего единиц: {total_count}")
print(f"Внесено: {paid:.2f} руб.")
print(f"Сдача: {change:.2f} руб.")
