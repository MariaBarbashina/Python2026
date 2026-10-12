# Лабораторная работа 11. Анализ todos.json и индивидуальный вариант 10

import json
from pathlib import Path

from analysis import (completion_counts, leaders_tasks, load_json, save_json,
                      select_tasks, task_ids, top_users, validate_todos)

FOLDER = Path(__file__).resolve().parent
TODOS_PATH = FOLDER / "todos.json"
LEADERS_PATH = FOLDER / "leaders.json"
SELECTED_PATH = FOLDER / "selected.json"


def read_integer(prompt, minimum):
    """Повторять ввод, пока не получено целое число не меньше minimum."""
    while True:
        text = input(prompt)
        try:
            number = int(text)
        except ValueError:
            print("Ошибка: введено не целое число")
            continue
        if number < minimum:
            print(f"Ошибка: число должно быть не меньше {minimum}")
            continue
        return number


def load_todos():
    """Прочитать и проверить todos.json. При ошибке вернуть None."""
    try:
        todos = load_json(TODOS_PATH)
        validate_todos(todos)
    except FileNotFoundError:
        print(f"Ошибка: файл {TODOS_PATH.name} не найден")
    except UnicodeError:
        print(f"Ошибка: файл {TODOS_PATH.name} не в кодировке UTF-8")
    except json.JSONDecodeError as error:
        # JSONDecodeError — подкласс ValueError, поэтому обрабатывается раньше
        print(f"Ошибка: некорректный JSON в {TODOS_PATH.name}: {error}")
    except ValueError as error:
        print(f"Ошибка структуры данных: {error}")
    except OSError as error:
        print(f"Ошибка доступа к файлу: {error}")
    else:
        return todos
    return None


def main():
    todos = load_todos()
    if todos is None:
        print("Результаты не изменены")
        return

    counts = completion_counts(todos)
    leaders = top_users(counts)
    leader_list = leaders_tasks(todos, leaders)

    print(f"Задач в наборе: {len(todos)}")
    print("Выполнено задач по пользователям:")
    for user_id in sorted(counts):
        print(f"  пользователь {user_id}: {counts[user_id]}")
    if leaders:
        print("Лидеры: " + ", ".join(str(user_id) for user_id in leaders))
    else:
        print("Лидеров нет")
    print(f"Выполненные задачи лидеров (id): {task_ids(leader_list)}")

    try:
        save_json(leader_list, LEADERS_PATH)
    except OSError as error:
        print(f"Ошибка записи {LEADERS_PATH.name}: {error}")
        return
    print(f"Сохранено в {LEADERS_PATH.name}")

    print()
    print("Вариант 10: задачи пользователя с длиной названия не меньше порога")
    user_id = read_integer("user_id (положительное целое): ", 1)
    threshold = read_integer("Минимальная длина названия (целое >= 0): ", 0)
    selected = select_tasks(todos, user_id, threshold)
    for todo in selected:
        print(f"  {todo['id']}: {todo['title']} (длина {len(todo['title'])})")
    print(f"Выбрано задач (id): {task_ids(selected)}")

    try:
        save_json(selected, SELECTED_PATH)
    except OSError as error:
        print(f"Ошибка записи {SELECTED_PATH.name}: {error}")
        return
    print(f"Сохранено в {SELECTED_PATH.name}")


if __name__ == "__main__":
    main()
