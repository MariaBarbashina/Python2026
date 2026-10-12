"""Лабораторная работа 9. Функции для обработки прямоугольных таблиц.

Функции не вызывают input() и print() и не изменяют полученную матрицу.
"""


def row_sums(matrix):
    """Вернуть список сумм строк; для [] вернуть []."""
    sums = []
    for row in matrix:
        sums.append(sum(row))
    return sums


def column_sums(matrix):
    """Вернуть список сумм столбцов; для [] вернуть [].

    Непустая матрица прямоугольная и имеет хотя бы один столбец.
    """
    if len(matrix) == 0:
        return []
    columns = len(matrix[0])
    sums = [0] * columns
    for row in matrix:
        for column in range(columns):
            sums[column] += row[column]
    return sums


def diagonal_pattern(size):
    """Вернуть квадратную таблицу size × size: на главной диагонали 0,
    выше неё 1, ниже неё 2. size — целое, не меньше 1."""
    pattern = []
    for row in range(size):
        pattern_row = []
        for column in range(size):
            if row == column:
                pattern_row.append(0)
            elif row < column:
                pattern_row.append(1)
            else:
                pattern_row.append(2)
        pattern.append(pattern_row)
    return pattern


def transform(matrix):
    """Вариант 10: вернуть новую матрицу той же формы, в которой элементы
    с модулем больше 4 заменены нулями. Остальные элементы сохраняются."""
    result = []
    for row in matrix:
        new_row = []
        for value in row:
            if abs(value) > 4:
                new_row.append(0)
            else:
                new_row.append(value)
        result.append(new_row)
    return result
