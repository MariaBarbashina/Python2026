"""Итоговый проект. Учёт печатных заказов (вариант 10). Консольное меню."""

import json
from pathlib import Path

from logic import (add_record, delete_record, find_records, get_record,
                   set_completed, sorted_records, statistics)
from storage import load_records, save_records

DATA_PATH = Path(__file__).resolve().parent / "data.json"
UNIT = "стр."

MENU = """
===== Учёт печатных заказов =====
1 — Показать заказы
2 — Добавить заказ
3 — Найти заказы по названию
4 — Изменить статус заказа
5 — Удалить заказ
6 — Статистика
7 — Сохранить данные
8 — Выход"""


# ---------- Оформление ----------

def status_text(completed):
    """Вернуть текст статуса заказа."""
    if completed:
        return "напечатан"
    return "не напечатан"


def format_record(record):
    """Вернуть строку с данными заказа для вывода."""
    return (f"ID {record['id']} | {record['title']} | {record['category']} | "
            f"{record['amount']} {UNIT} | {status_text(record['completed'])}")


def print_records(records):
    """Вывести записи по одной на строке."""
    for record in records:
        print(format_record(record))


# ---------- Ввод с повторением ----------

def read_text(prompt, error_message):
    """Запрашивать строку, пока она не станет непустой после strip()."""
    while True:
        text = input(prompt).strip()
        if text != "":
            return text
        print(f"Ошибка: {error_message}")


def read_int(prompt):
    """Запрашивать целое число, пока ввод не будет корректным."""
    while True:
        text = input(prompt).strip()
        try:
            return int(text)
        except ValueError:
            print("Ошибка: нужно ввести целое число")


def read_amount(prompt):
    """Запрашивать целое число не меньше 0."""
    while True:
        amount = read_int(prompt)
        if amount >= 0:
            return amount
        print("Ошибка: количество страниц не может быть отрицательным")


def ask_yes_no(prompt):
    """Повторять вопрос, пока не получен ответ «да» или «нет»."""
    while True:
        answer = input(prompt).strip().lower()
        if answer == "да":
            return True
        if answer == "нет":
            return False
        print("Ответьте «да» или «нет»")


# ---------- Команды меню ----------

def show_records(records):
    """1. Показать все записи по возрастанию ID."""
    if len(records) == 0:
        print("Нет записей")
        return
    print_records(sorted_records(records))


def add_command(records):
    """2. Добавить запись."""
    title = read_text("Название заказа: ", "название не может быть пустым")
    category = read_text("Категория (вид печати): ", "категория не может быть пустой")
    amount = read_amount("Количество страниц: ")
    record = add_record(records, title, category, amount)
    print(f"Добавлен заказ: {format_record(record)}")


def find_command(records):
    """3. Найти записи по подстроке названия."""
    query = input("Часть названия для поиска: ")
    try:
        found = find_records(records, query)
    except ValueError as error:
        print(f"Ошибка: {error}")
        return
    if len(found) == 0:
        print(f"Заказов с «{query.strip()}» в названии не найдено")
        return
    print(f"Найдено заказов: {len(found)}")
    print_records(found)


def status_command(records):
    """4. Явно установить статус заказа по ID."""
    record_id = read_int("ID заказа: ")
    if get_record(records, record_id) is None:
        print(f"Заказ с ID {record_id} не найден, данные не изменены")
        return
    print("1 — напечатан")
    print("2 — не напечатан")
    while True:
        choice = input("Новый статус: ").strip()
        if choice in ("1", "2"):
            break
        print("Ошибка: выберите 1 или 2")
    set_completed(records, record_id, choice == "1")
    print(f"Статус обновлён: {format_record(get_record(records, record_id))}")


def delete_command(records):
    """5. Удалить запись по ID после подтверждения «да»."""
    record_id = read_int("ID заказа для удаления: ")
    record = get_record(records, record_id)
    if record is None:
        print(f"Заказ с ID {record_id} не найден, список не изменён")
        return
    print(format_record(record))
    answer = input("Удалить этот заказ? Для подтверждения введите «да»: ")
    if answer.strip().lower() != "да":
        print("Удаление отменено")
        return
    delete_record(records, record_id)
    print(f"Заказ с ID {record_id} удалён")


def statistics_command(records):
    """6. Показать статистику по текущему списку."""
    stats = statistics(records)
    print(f"Всего заказов: {stats['total']}")
    print(f"Напечатано: {stats['completed']}")
    print(f"Не напечатано: {stats['not_completed']}")
    print(f"Всего страниц: {stats['amount_total']} {UNIT}")
    print("Страниц по категориям:")
    if len(stats["by_category"]) == 0:
        print("  нет категорий")
    for category in sorted(stats["by_category"]):
        print(f"  {category}: {stats['by_category'][category]} {UNIT}")


def save_command(records):
    """7. Сохранить данные. Вернуть True, если запись прошла успешно."""
    try:
        save_records(DATA_PATH, records)
    except OSError as error:
        print(f"Ошибка сохранения: {error}")
        print("Данные не сохранены")
        return False
    print(f"Данные сохранены в {DATA_PATH.name}")
    return True


def exit_command(records):
    """8. Выход. Вернуть True, если программу можно завершить."""
    if ask_yes_no("Сохранить данные перед выходом? (да/нет): "):
        return save_command(records)
    return True


# ---------- Запуск ----------

def load_data():
    """Загрузить и проверить data.json.

    Вернуть список записей; если файл повреждён — None (файл не меняется).
    """
    try:
        records = load_records(DATA_PATH)
    except FileNotFoundError:
        print(f"Файл {DATA_PATH.name} не найден, начинаем с пустого списка")
        return []
    except UnicodeError:
        print(f"Ошибка: файл {DATA_PATH.name} не в кодировке UTF-8")
    except json.JSONDecodeError as error:
        print(f"Ошибка: файл {DATA_PATH.name} повреждён (некорректный JSON): {error}")
    except ValueError as error:
        print(f"Ошибка структуры данных в {DATA_PATH.name}: {error}")
    except OSError as error:
        print(f"Ошибка доступа к {DATA_PATH.name}: {error}")
    else:
        print(f"Загружено заказов: {len(records)}")
        return records
    print("Запуск прекращён, файл не изменён. Исправьте файл и запустите программу снова")
    return None


def main():
    records = load_data()
    if records is None:
        return

    commands = {
        "1": show_records,
        "2": add_command,
        "3": find_command,
        "4": status_command,
        "5": delete_command,
        "6": statistics_command,
        "7": save_command,
    }
    while True:
        print(MENU)
        command = input("Выберите команду: ").strip()
        print()
        if command == "8":
            if exit_command(records):
                print("Работа завершена")
                break
            print("Выход отменён, продолжаем работу")
        elif command in commands:
            commands[command](records)
        else:
            print("Неизвестная команда, выберите пункт от 1 до 8")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print()
        print("Работа прервана, несохранённые изменения потеряны")
