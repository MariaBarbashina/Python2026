# Лабораторная работа 11. Автоматические проверки модуля analysis.py
# Сеть не используется; файлы создаются во временной папке.

import copy
from pathlib import Path
from tempfile import TemporaryDirectory

from analysis import (completion_counts, leaders_tasks, load_json, save_json,
                      select_tasks, task_ids, top_users, validate_todos)

TODOS = [
    {"id": 1, "userId": 5, "title": "Ввод", "completed": True},
    {"id": 2, "userId": 5, "title": "Циклы", "completed": False},
    {"id": 3, "userId": 10, "title": "Строки", "completed": True},
    {"id": 4, "userId": 10, "title": "Файлы", "completed": True},
    {"id": 5, "userId": 5, "title": "Списки", "completed": True},
]
TODOS_COPY = copy.deepcopy(TODOS)


def expect_value_error(data):
    """Проверить, что validate_todos(data) выбрасывает ValueError."""
    try:
        validate_todos(data)
    except ValueError:
        pass
    else:
        assert False, f"Ошибка не обнаружена: {data!r}"


# ---------- Учебный набор ----------
folder = Path(__file__).resolve().parent
assert load_json(folder / "todos.json") == TODOS, "todos.json отличается от образца"
validate_todos(TODOS)
counts = completion_counts(TODOS)
assert counts == {5: 2, 10: 2}
leaders = top_users(counts)
assert leaders == [5, 10]
assert task_ids(leaders_tasks(TODOS, leaders)) == [1, 3, 4, 5]
print("Проверки учебного набора пройдены")

# ---------- Пустой набор и набор без выполненных задач ----------
validate_todos([])
assert completion_counts([]) == {}
assert top_users({}) == []
assert leaders_tasks([], []) == []

not_done = [
    {"id": 1, "userId": 3, "title": "А", "completed": False},
    {"id": 2, "userId": 4, "title": "Б", "completed": False},
]
validate_todos(not_done)
assert completion_counts(not_done) == {3: 0, 4: 0}
assert top_users(completion_counts(not_done)) == []
assert leaders_tasks(not_done, top_users(completion_counts(not_done))) == []
print("Проверки пустых наборов пройдены")

# ---------- Один лидер и несколько лидеров ----------
assert top_users({1: 3, 2: 1, 3: 0}) == [1]
assert top_users({7: 2, 2: 2, 4: 1}) == [2, 7]   # сортировка числовая
assert top_users({10: 1, 9: 1}) == [9, 10]       # числа, а не строки: 9 < 10
single = [
    {"id": 1, "userId": 1, "title": "А", "completed": True},
    {"id": 2, "userId": 2, "title": "Б", "completed": False},
    {"id": 3, "userId": 1, "title": "В", "completed": True},
]
assert top_users(completion_counts(single)) == [1]
assert task_ids(leaders_tasks(single, [1])) == [1, 3]
print("Проверки лидеров пройдены")

# ---------- Вариант 10: длина названия не меньше порога ----------
assert task_ids(select_tasks(TODOS, 5, 5)) == [2, 5]         # пример из таблицы
assert task_ids(select_tasks(TODOS, 5, 4)) == [1, 2, 5]      # граница: «Ввод» длины 4 входит
assert task_ids(select_tasks(TODOS, 5, 6)) == [5]            # граница: «Списки» длины 6 входит
assert task_ids(select_tasks(TODOS, 10, 6)) == [3]
assert task_ids(select_tasks(TODOS, 5, 0)) == [1, 2, 5]      # порог 0 — все задачи пользователя
assert select_tasks(TODOS, 99, 1) == []                      # неизвестный пользователь
assert select_tasks(TODOS, 5, 7) == []                       # непустой набор без совпадений
assert select_tasks([], 5, 1) == []
try:
    select_tasks(TODOS, 5, None)
except ValueError:
    pass
else:
    assert False, "Ошибка не обнаружена"
assert TODOS == TODOS_COPY, "исходные записи изменились"
print("Проверки варианта 10 пройдены")

# ---------- Ошибки структуры ----------
expect_value_error({"id": 1, "userId": 5, "title": "Ввод", "completed": True})  # объект вместо списка
expect_value_error([TODOS[0], {"id": 1, "userId": 6, "title": "X", "completed": False}])  # повторный id
expect_value_error([{"id": 1, "title": "Ввод", "completed": True}])               # нет userId
expect_value_error([{"id": 1, "userId": 5, "title": "Ввод", "completed": "false"}])  # completed строкой
expect_value_error([{"id": True, "userId": 5, "title": "Ввод", "completed": True}])  # id=true
expect_value_error([{"id": 0, "userId": 5, "title": "Ввод", "completed": True}])     # id не положительный
expect_value_error([{"id": 1, "userId": 5, "title": "   ", "completed": True}])      # пустой title
expect_value_error([{"id": 1, "userId": 5, "title": 7, "completed": True}])          # title не строка
expect_value_error([{"id": 1, "userId": 5, "title": "Ввод"}])                        # нет completed
expect_value_error(["не объект"])
# Дополнительные ключи допустимы
validate_todos([{"id": 1, "userId": 5, "title": "Ввод", "completed": True, "note": None}])
print("Проверки ошибок структуры пройдены")

# ---------- Запись и повторное чтение JSON ----------
with TemporaryDirectory() as directory:
    path = Path(directory) / "selected.json"
    selected = select_tasks(TODOS, 5, 5)
    save_json(selected, path)
    assert load_json(path) == selected

    path = Path(directory) / "leaders.json"
    leader_list = leaders_tasks(TODOS, [5, 10])
    save_json(leader_list, path)
    assert load_json(path) == leader_list
print("Проверки записи и чтения JSON пройдены")

print("Все проверки пройдены")
