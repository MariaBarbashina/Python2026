"""Лабораторная работа 10. Чтение таблицы из файла, вариант 10, экспорт CSV.

Функции не выполняют ввод и вывод в консоль. О проблемах с данными они
сообщают исключениями, а основная программа показывает понятное сообщение.
"""

import csv


def parse_int(text, line_number):
    """Преобразовать text в int или выбросить ValueError с номером строки."""
    try:
        return int(text)
    except ValueError:
        raise ValueError(
            f"Строка {line_number}: «{text}» не является целым числом"
        ) from None


def read_matrix(path):
    """Прочитать матрицу из текстового файла UTF-8.

    Формат: первая строка — количество строк и столбцов (положительные
    целые), далее ровно указанное число строк по указанному числу целых.
    Пустые и лишние строки — ошибка; один перевод строки в конце допустим.
    Ошибки формата — ValueError, отсутствие файла — FileNotFoundError.
    """
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

    if text == "":
        raise ValueError("Файл пуст")
    if text.endswith("\n"):
        text = text[:-1]   # один завершающий перевод строки допустим
    lines = text.split("\n")

    header = lines[0].split()
    if len(header) != 2:
        raise ValueError(
            "Строка 1: заголовок должен содержать два числа — "
            "количество строк и столбцов"
        )
    rows = parse_int(header[0], 1)
    columns = parse_int(header[1], 1)
    if rows <= 0 or columns <= 0:
        raise ValueError(
            "Строка 1: количество строк и столбцов должно быть больше нуля"
        )

    data_lines = lines[1:]
    if len(data_lines) < rows:
        raise ValueError(
            f"Ожидалось строк данных: {rows}, найдено: {len(data_lines)}"
        )
    if len(data_lines) > rows:
        raise ValueError(
            f"Строка {rows + 2}: лишняя строка, ожидалось строк данных: {rows}"
        )

    matrix = []
    for index, line in enumerate(data_lines):
        line_number = index + 2
        parts = line.split()
        if len(parts) == 0:
            raise ValueError(f"Строка {line_number}: пустая строка")
        if len(parts) != columns:
            raise ValueError(
                f"Строка {line_number}: ожидалось чисел: {columns}, "
                f"получено: {len(parts)}"
            )
        row = []
        for part in parts:
            row.append(parse_int(part, line_number))
        matrix.append(row)
    return matrix


def selected_sum(matrix):
    """Вариант 10: вернуть сумму элементов первого столбца (0 для [])."""
    total = 0
    for row in matrix:
        total += row[0]
    return total


def format_report(row_totals, column_totals, variant_result):
    """Вернуть текст отчёта."""
    return (
        "Суммы строк: " + " ".join(str(value) for value in row_totals) + "\n"
        + "Суммы столбцов: "
        + " ".join(str(value) for value in column_totals) + "\n"
        + f"Результат варианта: {variant_result}\n"
    )


def export_csv(matrix, path):
    """Дополнительное задание: сохранить матрицу в CSV модулем csv."""
    with open(path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(matrix)
