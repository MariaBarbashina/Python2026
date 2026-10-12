# Лабораторная работа 10. Автоматические проверки модуля files_lab.py
# Все файлы создаются во временной папке.

import csv
from pathlib import Path
from tempfile import TemporaryDirectory

from files_lab import export_csv, format_report, read_matrix, selected_sum


def expect_value_error(path, expected_part=None):
    """Проверить, что read_matrix(path) выбрасывает ValueError.

    Если задан expected_part, он должен входить в текст ошибки.
    """
    try:
        read_matrix(path)
    except ValueError as error:
        if expected_part is not None:
            assert expected_part in str(error), f"В сообщении нет «{expected_part}»: {error}"
    else:
        assert False, "Ошибка не обнаружена"


with TemporaryDirectory() as directory:
    path = Path(directory) / "matrix.txt"

    # Пример из методички
    path.write_text("1 2\n7 -1\n", encoding="utf-8")
    assert read_matrix(path) == [[7, -1]]

    # Учебный файл matrix.txt
    path.write_text("2 3\n1 -2 3\n4 0 -6\n", encoding="utf-8")
    assert read_matrix(path) == [[1, -2, 3], [4, 0, -6]]

    # Без завершающего перевода строки — тоже корректно
    path.write_text("2 3\n1 -2 3\n4 0 -6", encoding="utf-8")
    assert read_matrix(path) == [[1, -2, 3], [4, 0, -6]]

    # 1×1 с нулём
    path.write_text("1 1\n0\n", encoding="utf-8")
    assert read_matrix(path) == [[0]]
    print("Проверки корректных файлов пройдены")

    # Пустой файл
    path.write_text("", encoding="utf-8")
    expect_value_error(path)

    # Заголовок 0 3
    path.write_text("0 3\n", encoding="utf-8")
    expect_value_error(path, "Строка 1")

    # Заголовок из одного числа и нечисловой заголовок
    path.write_text("2\n1 2\n", encoding="utf-8")
    expect_value_error(path, "Строка 1")
    path.write_text("a 2\n1 2\n", encoding="utf-8")
    expect_value_error(path, "Строка 1")

    # Заголовок 1 2, строка «1» — мало чисел
    path.write_text("1 2\n1\n", encoding="utf-8")
    expect_value_error(path, "Строка 2")

    # Заголовок 1 2, строка «1 x» — нечисловая ячейка
    path.write_text("1 2\n1 x\n", encoding="utf-8")
    expect_value_error(path, "Строка 2")

    # Заголовок 1 1, две строки данных — лишняя строка
    path.write_text("1 1\n5\n6\n", encoding="utf-8")
    expect_value_error(path, "Строка 3")

    # Строк данных меньше, чем указано в заголовке
    path.write_text("3 1\n5\n6\n", encoding="utf-8")
    expect_value_error(path)

    # Пустая строка в середине и лишняя пустая строка в конце
    path.write_text("2 1\n\n5\n", encoding="utf-8")
    expect_value_error(path, "Строка 2")
    path.write_text("1 1\n5\n\n", encoding="utf-8")
    expect_value_error(path, "Строка 3")
    print("Проверки ошибок формата пройдены")

    # Неправильная кодировка: UnicodeDecodeError — тоже подкласс ValueError
    path.write_bytes("2 1\nдва\n1\n".encode("cp1251"))
    try:
        read_matrix(path)
    except UnicodeError:
        pass
    else:
        assert False, "Ошибка кодировки не обнаружена"

    # Отсутствующий путь
    try:
        read_matrix(Path(directory) / "missing.txt")
    except FileNotFoundError:
        pass
    else:
        assert False, "Ошибка не обнаружена"
    print("Проверки кодировки и отсутствующего файла пройдены")

    # Дополнительное задание: экспорт в CSV и чтение модулем csv
    csv_path = Path(directory) / "matrix.csv"
    export_csv([[1, -2, 3], [4, 0, -6]], csv_path)
    with open(csv_path, "r", encoding="utf-8", newline="") as file:
        rows = list(csv.reader(file))
    assert rows == [["1", "-2", "3"], ["4", "0", "-6"]]
    print("Проверка экспорта CSV пройдена")

# ---------- Вариант 10: сумма первого столбца ----------
assert selected_sum([[1, -2, 3], [4, 0, -6]]) == 5
assert selected_sum([[7]]) == 7               # 1×1: элемент учитывается один раз
assert selected_sum([[-3], [3]]) == 0         # один столбец
assert selected_sum([[2, 100, 100]]) == 2     # одна строка
assert selected_sum([]) == 0                  # нет элементов
print("Проверки варианта 10 пройдены")

# ---------- Формат отчёта ----------
assert format_report([2, -2], [5, -2, -3], 5) == (
    "Суммы строк: 2 -2\n"
    "Суммы столбцов: 5 -2 -3\n"
    "Результат варианта: 5\n"
)
print("Проверка формата отчёта пройдена")

print("Все проверки пройдены")
