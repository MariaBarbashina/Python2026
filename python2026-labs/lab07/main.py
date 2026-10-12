# Лабораторная работа 7. Демонстрация функций модуля functions.py

from functions import (average, is_palindrome, normalize_text,
                       select_numbers, sum_digits)


def read_numbers(prompt):
    """Прочитать строку целых чисел через пробел и вернуть список."""
    numbers = []
    for part in input(prompt).split():
        numbers.append(int(part))
    return numbers


def main():
    number = int(input("Целое число: "))
    print(f"Сумма цифр: {sum_digits(number)}")

    numbers = read_numbers("Целые числа через пробел: ")
    mean = average(numbers)
    if mean is None:
        print("Нет данных")
    else:
        print(f"Среднее: {mean:.2f}")

    text = input("Произвольный текст: ")
    print(f"Нормализованный текст: '{normalize_text(text)}'")
    if is_palindrome(text):
        print("Палиндром: да")
    else:
        print("Палиндром: нет")

    threshold = int(input("Порог (целое, не меньше 0): "))
    selected = select_numbers(numbers, threshold)
    print(f"Числа от -{threshold} до 0 включительно: {selected}")


if __name__ == "__main__":
    main()
