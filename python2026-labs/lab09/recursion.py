# Лабораторная работа 9. Дополнительный модуль: рекурсия
# Факториал рекурсивно и итеративно, трассировка factorial(3).


def factorial(number):
    """Рекурсивный факториал. Аргумент — целое число от 0 до 20."""
    if number == 0:          # базовый случай
        return 1
    return number * factorial(number - 1)   # шаг приближает к базовому случаю


def factorial_iterative(number):
    """Итеративный факториал. Аргумент — целое число от 0 до 20."""
    result = 1
    for factor in range(2, number + 1):
        result *= factor
    return result


def factorial_traced(number, depth=0):
    """Рекурсивный факториал с выводом вызовов и возвратов."""
    indent = "  " * depth
    print(f"{indent}вызов factorial({number})")
    if number == 0:
        result = 1
    else:
        result = number * factorial_traced(number - 1, depth + 1)
    print(f"{indent}возврат {result} из factorial({number})")
    return result


def main():
    assert factorial(0) == 1
    assert factorial(5) == 120

    print("Трассировка factorial(3):")
    factorial_traced(3)

    print()
    print("Сравнение рекурсивной и итеративной версий:")
    for number in range(21):
        recursive = factorial(number)
        iterative = factorial_iterative(number)
        assert recursive == iterative
        print(f"{number}! = {recursive}")
    print("Результаты для 0–20 совпадают")


if __name__ == "__main__":
    main()
