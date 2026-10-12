"""Лабораторная работа 7. Модуль функций (вариант 10).

Функции модуля не вызывают input() и print(): они получают данные
через параметры и возвращают результат через return.
"""


def sum_digits(number):
    """Вернуть сумму цифр модуля целого числа; для 0 результат 0."""
    number = abs(number)
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total


def average(numbers):
    """Вернуть среднее списка чисел или None для пустого списка.

    Исходный список не изменяется.
    """
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)


def normalize_text(text):
    """Вернуть текст в нижнем регистре без пробелов по краям,
    с одним пробелом между словами."""
    return " ".join(text.lower().split())


def select_numbers(numbers, threshold):
    """Вариант 10: вернуть новый список чисел от -threshold до 0 включительно.

    Порядок и повторы сохраняются, исходный список не изменяется.
    threshold — целое неотрицательное число.
    """
    selected = []
    for number in numbers:
        if -threshold <= number <= 0:
            selected.append(number)
    return selected


def is_palindrome(text):
    """Дополнительное задание: проверить текст на палиндром по правилам
    работы №5 (регистр и обычные пробелы игнорируются, остальные символы
    сравниваются как есть). Для пустого текста вернуть False."""
    cleaned = text.lower().replace(" ", "")
    if cleaned == "":
        return False
    return cleaned == cleaned[::-1]
