# Лабораторная работа 3. Задание 2: калькулятор (без eval)

first = float(input("Первое число: "))
second = float(input("Второе число: "))
operation = input("Операция (+, -, *, /): ").strip()

if operation == "+":
    print(f"Результат: {first + second:.2f}")
elif operation == "-":
    print(f"Результат: {first - second:.2f}")
elif operation == "*":
    print(f"Результат: {first * second:.2f}")
elif operation == "/":
    if second == 0:
        print("Деление на ноль запрещено")
    else:
        print(f"Результат: {first / second:.2f}")
else:
    print("Неизвестная операция")
