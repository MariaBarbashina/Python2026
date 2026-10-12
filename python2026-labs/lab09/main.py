# Лабораторная работа 9. Ввод таблицы, суммы, преобразование и узор

from table import column_sums, diagonal_pattern, row_sums, transform


def read_positive(prompt):
    """Запрашивать целое число, пока оно не станет больше нуля."""
    value = int(input(prompt))
    while value <= 0:
        print("Число должно быть больше нуля")
        value = int(input(prompt))
    return value


def read_matrix(rows, columns):
    """Прочитать прямоугольную таблицу с проверкой длины каждой строки."""
    matrix = []
    for index in range(rows):
        row = [int(part) for part in input(f"Строка {index + 1}: ").split()]
        while len(row) != columns:
            print(f"Нужно ровно {columns} чисел")
            row = [int(part) for part in input("Повторите строку: ").split()]
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    """Вывести таблицу построчно, элементы через пробел."""
    for row in matrix:
        print(*row)


def main():
    rows = read_positive("Количество строк: ")
    columns = read_positive("Количество столбцов: ")
    matrix = read_matrix(rows, columns)

    print("Исходная таблица:")
    print_matrix(matrix)
    print(f"Суммы строк: {row_sums(matrix)}")
    print(f"Суммы столбцов: {column_sums(matrix)}")

    transformed = transform(matrix)
    print("Новая таблица (элементы с модулем больше 4 заменены нулями):")
    print_matrix(transformed)
    print("Исходная таблица после преобразования (не изменилась):")
    print_matrix(matrix)

    size = read_positive("Размер диагонального узора: ")
    print("Диагональный узор:")
    print_matrix(diagonal_pattern(size))


if __name__ == "__main__":
    main()
