# Лабораторная работа 10. Отчёт по таблице из файла и надёжный ввод размера

from pathlib import Path

from files_lab import export_csv, format_report, read_matrix, selected_sum
from table import column_sums, diagonal_pattern, row_sums

FOLDER = Path(__file__).resolve().parent
MATRIX_PATH = FOLDER / "matrix.txt"
REPORT_PATH = FOLDER / "report.txt"
CSV_PATH = FOLDER / "matrix.csv"


def read_positive_integer(prompt="Положительное целое число: "):
    """Повторять ввод, пока не получено целое число больше нуля."""
    while True:
        text = input(prompt)
        try:
            number = int(text)
        except ValueError:
            print("Ошибка: введено не целое число")
            continue
        if number <= 0:
            print("Ошибка: число должно быть больше нуля")
            continue
        return number


def build_report():
    """Прочитать matrix.txt, проверить данные и только затем записать отчёт.

    При любой ошибке чтения или проверки report.txt не открывается для
    записи, поэтому прежний отчёт остаётся без изменений.
    """
    try:
        matrix = read_matrix(MATRIX_PATH)
    except FileNotFoundError:
        print(f"Ошибка: файл {MATRIX_PATH.name} не найден")
        return
    except UnicodeError:
        print(f"Ошибка: файл {MATRIX_PATH.name} не в кодировке UTF-8")
        return
    except ValueError as error:
        print(f"Ошибка формата в {MATRIX_PATH.name}: {error}")
        return
    except OSError as error:
        print(f"Ошибка доступа к {MATRIX_PATH.name}: {error}")
        return

    report = format_report(row_sums(matrix), column_sums(matrix),
                           selected_sum(matrix))
    try:
        with open(REPORT_PATH, "w", encoding="utf-8") as file:
            file.write(report)
        export_csv(matrix, CSV_PATH)
    except OSError as error:
        print(f"Ошибка записи результата: {error}")
        return

    print(f"Таблица из {MATRIX_PATH.name}: {matrix}")
    print(f"Отчёт сохранён в {REPORT_PATH.name}:")
    print(report, end="")
    print(f"Таблица экспортирована в {CSV_PATH.name}")


def main():
    build_report()

    print()
    size = read_positive_integer("Размер диагонального узора: ")
    for row in diagonal_pattern(size):
        print(*row)


if __name__ == "__main__":
    main()
