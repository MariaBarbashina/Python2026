# Лабораторная работа 9. Автоматические проверки модуля table.py

from table import column_sums, diagonal_pattern, row_sums, transform

# Таблица 2×3: выявляет перепутанные строки и столбцы
matrix = [[1, 2, 3], [4, 5, 6]]
assert row_sums(matrix) == [6, 15]
assert column_sums(matrix) == [5, 7, 9]

# Таблица 1×1 и узор размера 1
assert row_sums([[7]]) == [7]
assert column_sums([[7]]) == [7]
assert diagonal_pattern(1) == [[0]]

# Один столбец
assert row_sums([[1], [-1], [0]]) == [1, -1, 0]
assert column_sums([[1], [-1], [0]]) == [0]

# Одна строка
assert row_sums([[1, 2, 3]]) == [6]
assert column_sums([[1, 2, 3]]) == [1, 2, 3]

# Пустая матрица
assert row_sums([]) == []
assert column_sums([]) == []
assert transform([]) == []

# Узор размера 3 точно совпадает с образцом
assert diagonal_pattern(3) == [
    [0, 1, 1],
    [2, 0, 1],
    [2, 2, 0],
]
assert diagonal_pattern(2) == [[0, 1], [2, 0]]

# Строки узора — независимые списки
pattern = diagonal_pattern(3)
pattern[0][1] = 9
assert pattern[1][1] == 0 and pattern[2][1] == 2
print("Проверки сумм и узора пройдены")

# ---------- Вариант 10: модуль больше 4 → 0 ----------
source = [[-2, 0, 3], [4, -5, 6]]
source_copy = [row.copy() for row in source]
result = transform(source)
assert result == [[-2, 0, 3], [4, 0, 0]]

# Граница: модуль 4 не заменяется, модуль 5 заменяется
assert transform([[4, -4, 5, -5]]) == [[4, -4, 0, 0]]
# Нет подходящих элементов — таблица не меняется
assert transform([[1, -2], [3, 0]]) == [[1, -2], [3, 0]]
# Все элементы подходят
assert transform([[10], [-7]]) == [[0], [0]]

# Исходная матрица не изменилась, результат независим от неё
assert source == source_copy
result[0][0] = 100
assert source == source_copy, "изменение результата затронуло исходную матрицу"
assert source[0][0] == -2

# Функции сумм не меняют матрицу
row_sums(source)
column_sums(source)
assert source == source_copy
print("Проверки варианта 10 пройдены")

print("Все проверки пройдены")
