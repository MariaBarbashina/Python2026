"""Лабораторная работа 11. Проверка и анализ списка задач (вариант 10).

Модуль не выполняет сетевых запросов и консольного ввода-вывода.
"""

import json


def load_json(path):
    """Прочитать JSON из файла в кодировке UTF-8."""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(data, path):
    """Сохранить данные в JSON (UTF-8, читаемая кириллица, отступ 2)."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
        file.write("\n")


def validate_todos(data):
    """Проверить структуру набора задач; при нарушении выбросить ValueError.

    Корень — список; каждая запись — словарь с положительными целыми id и
    userId, непустой строкой title и логическим completed; id уникальны.
    Дополнительные ключи допустимы.
    """
    if type(data) is not list:
        raise ValueError("Корень JSON должен быть списком")

    seen_ids = set()
    for index, todo in enumerate(data):
        place = f"Запись {index}"
        if type(todo) is not dict:
            raise ValueError(f"{place}: ожидался объект")

        for key in ("id", "userId"):
            if key not in todo:
                raise ValueError(f"{place}: нет поля {key}")
            value = todo[key]
            # type(...) is int отсекает True/False, которые проходят isinstance
            if type(value) is not int or value <= 0:
                raise ValueError(
                    f"{place}: поле {key} должно быть положительным целым"
                )

        if "title" not in todo:
            raise ValueError(f"{place}: нет поля title")
        title = todo["title"]
        if type(title) is not str or title.strip() == "":
            raise ValueError(f"{place}: поле title должно быть непустой строкой")

        if "completed" not in todo:
            raise ValueError(f"{place}: нет поля completed")
        if type(todo["completed"]) is not bool:
            raise ValueError(f"{place}: поле completed должно быть true или false")

        if todo["id"] in seen_ids:
            raise ValueError(f"{place}: повторный id {todo['id']}")
        seen_ids.add(todo["id"])


def completion_counts(todos):
    """Вернуть словарь «userId → количество выполненных задач» для всех
    пользователей набора, включая пользователей с нулём."""
    counts = {}
    for todo in todos:
        user_id = todo["userId"]
        counts[user_id] = counts.get(user_id, 0)
        if todo["completed"]:
            counts[user_id] += 1
    return counts


def top_users(counts):
    """Вернуть отсортированный список userId с максимальным количеством
    выполненных задач; для пустого словаря или максимума 0 вернуть []."""
    if len(counts) == 0:
        return []
    maximum = max(counts.values())
    if maximum == 0:
        return []
    leaders = []
    for user_id, count in counts.items():
        if count == maximum:
            leaders.append(user_id)
    return sorted(leaders)


def leaders_tasks(todos, leaders):
    """Вернуть выполненные задачи пользователей-лидеров в исходном порядке."""
    result = []
    for todo in todos:
        if todo["userId"] in leaders and todo["completed"]:
            result.append(todo)
    return result


def select_tasks(todos, user_id, parameter=None):
    """Вариант 10: задачи пользователя user_id с длиной названия не меньше
    порога parameter (целое неотрицательное). Порядок сохраняется,
    исходные записи не изменяются."""
    if type(parameter) is not int or parameter < 0:
        raise ValueError("Порог должен быть целым неотрицательным числом")
    result = []
    for todo in todos:
        if todo["userId"] == user_id and len(todo["title"]) >= parameter:
            result.append(todo)
    return result


def task_ids(todos):
    """Вернуть список id задач в исходном порядке."""
    ids = []
    for todo in todos:
        ids.append(todo["id"])
    return ids
