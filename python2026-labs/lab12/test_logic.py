# Итоговый проект. Автоматические проверки logic.py (без меню и файлов)

import copy

from logic import (add_record, delete_record, find_records, get_record,
                   next_id, set_completed, sorted_records, statistics,
                   validate_records)


def expect_value_error(function, *args):
    """Проверить, что вызов function(*args) выбрасывает ValueError."""
    try:
        function(*args)
    except ValueError:
        pass
    else:
        assert False, f"Ошибка не обнаружена: {function.__name__}{args!r}"


def sample_records():
    """Вернуть новый вымышленный набор из 5 заказов."""
    return [
        {"id": 1, "title": "Курсовая работа по истории", "category": "переплёт", "amount": 45, "completed": True},
        {"id": 2, "title": "Рекламные буклеты для кафе", "category": "цветная печать", "amount": 120, "completed": False},
        {"id": 3, "title": "Методичка по Python", "category": "чёрно-белая печать", "amount": 80, "completed": True},
        {"id": 4, "title": "Афиши для концерта", "category": "цветная печать", "amount": 30, "completed": False},
        {"id": 5, "title": "Дипломная работа", "category": "переплёт", "amount": 90, "completed": False},
    ]


# ---------- Пустой список ----------
empty = []
validate_records(empty)
assert next_id(empty) == 1
assert sorted_records(empty) == []
assert statistics(empty) == {
    "total": 0, "completed": 0, "not_completed": 0,
    "amount_total": 0, "by_category": {},
}
assert find_records(empty, "py") == []
assert set_completed(empty, 1, True) is False
assert delete_record(empty, 1) is False
assert empty == []
print("Проверки пустого списка пройдены")

# ---------- Сценарий: записи с количеством 4 и 2, вторая завершена ----------
records = []
add_record(records, "Первый заказ", "переплёт", 4)
add_record(records, "Второй заказ", "переплёт", 2)
assert set_completed(records, 2, True) is True
stats = statistics(records)
assert stats["total"] == 2
assert stats["completed"] == 1
assert stats["not_completed"] == 1
assert stats["amount_total"] == 6
print("Проверка сценария «4 и 2» пройдена")

# ---------- Добавление ----------
records = []
record = add_record(records, "  Python  ", "  чёрно-белая печать ", 0)
assert record == {"id": 1, "title": "Python", "category": "чёрно-белая печать",
                  "amount": 0, "completed": False}
assert records == [record]
# Одинаковые названия разрешены, id различаются
second = add_record(records, "Python", "переплёт", 10)
assert second["id"] == 2 and second["title"] == "Python"
validate_records(records)
# Некорректные данные не добавляют запись
before = copy.deepcopy(records)
expect_value_error(add_record, records, "", "переплёт", 5)
expect_value_error(add_record, records, "   ", "переплёт", 5)
expect_value_error(add_record, records, "Заказ", "  ", 5)
expect_value_error(add_record, records, "Заказ", "переплёт", -1)
expect_value_error(add_record, records, "Заказ", "переплёт", "abc")
expect_value_error(add_record, records, "Заказ", "переплёт", 2.5)
expect_value_error(add_record, records, "Заказ", "переплёт", True)
assert records == before, "при ошибке появилась лишняя запись"
print("Проверки добавления пройдены")

# ---------- Удаление и следующий id ----------
records = []
add_record(records, "Первый", "переплёт", 1)
add_record(records, "Второй", "переплёт", 2)
assert delete_record(records, 1) is True
assert [item["id"] for item in records] == [2]      # оставшаяся запись сохранила id 2
assert add_record(records, "Третий", "переплёт", 3)["id"] == 3
assert delete_record(records, 99) is False          # неизвестный id
assert [item["id"] for item in records] == [2, 3]
# Удаление записи с максимальным id: новый id = максимум оставшихся + 1
assert delete_record(records, 3) is True
assert next_id(records) == 3
print("Проверки удаления пройдены")

# ---------- Изменение статуса ----------
records = sample_records()
before = copy.deepcopy(records)
assert set_completed(records, 42, True) is False    # неизвестный id
assert records == before, "данные изменились при неизвестном id"
assert set_completed(records, 2, True) is True
assert get_record(records, 2)["completed"] is True
assert set_completed(records, 2, True) is True      # повторная установка того же значения
assert set_completed(records, 1, False) is True
assert get_record(records, 1)["completed"] is False
expect_value_error(set_completed, records, 1, "да")
print("Проверки статуса пройдены")

# ---------- Поиск ----------
records = sample_records()
before = copy.deepcopy(records)
assert [item["id"] for item in find_records(records, "PY")] == [3]   # без учёта регистра
assert [item["id"] for item in find_records(records, "работа")] == [1, 5]
assert [item["id"] for item in find_records(records, "  для  ")] == [2, 4]
assert find_records(records, "календарь") == []
expect_value_error(find_records, records, "")
expect_value_error(find_records, records, "   ")
assert records == before, "поиск изменил данные"
# Результат по возрастанию id даже при перемешанном списке
mixed = [records[4], records[0], records[2]]
assert [item["id"] for item in find_records(mixed, "а")] == [1, 3, 5]
assert [item["id"] for item in sorted_records(mixed)] == [1, 3, 5]
print("Проверки поиска пройдены")

# ---------- Статистика по категориям ----------
records = sample_records()
before = copy.deepcopy(records)
assert statistics(records) == {
    "total": 5,
    "completed": 2,
    "not_completed": 3,
    "amount_total": 365,
    "by_category": {"переплёт": 135, "цветная печать": 150, "чёрно-белая печать": 80},
}
assert records == before, "статистика изменила данные"
# Две категории; категории сравниваются после удаления краевых пробелов
two = [
    {"id": 1, "title": "А", "category": " переплёт ", "amount": 3, "completed": True},
    {"id": 2, "title": "Б", "category": "переплёт", "amount": 4, "completed": False},
    {"id": 3, "title": "В", "category": "цветная печать", "amount": 5, "completed": False},
]
assert statistics(two)["by_category"] == {"переплёт": 7, "цветная печать": 5}
print("Проверки статистики пройдены")

# ---------- Строгие типы при проверке набора ----------
good = {"id": 1, "title": "А", "category": "переплёт", "amount": 1, "completed": False}


def with_change(**changes):
    """Вернуть список из одной записи good с изменёнными полями."""
    record = dict(good)
    record.update(changes)
    return [record]


def without(key):
    """Вернуть список из одной записи good без поля key."""
    record = dict(good)
    del record[key]
    return [record]


validate_records([good])
validate_records(with_change(note="дополнительный ключ", extra=None))
expect_value_error(validate_records, {"id": 1})                 # корень не список
expect_value_error(validate_records, ["не объект"])
for key in ("id", "title", "category", "amount", "completed"):
    expect_value_error(validate_records, without(key))
expect_value_error(validate_records, with_change(id=True))       # bool вместо id
expect_value_error(validate_records, with_change(id=0))
expect_value_error(validate_records, with_change(id="1"))
expect_value_error(validate_records, with_change(title="   "))
expect_value_error(validate_records, with_change(title=5))
expect_value_error(validate_records, with_change(category=""))
expect_value_error(validate_records, with_change(amount=True))   # bool вместо amount
expect_value_error(validate_records, with_change(amount=-1))
expect_value_error(validate_records, with_change(amount=1.5))
expect_value_error(validate_records, with_change(amount="10"))
expect_value_error(validate_records, with_change(completed="false"))
expect_value_error(validate_records, with_change(completed=0))
expect_value_error(validate_records, with_change(completed=None))
expect_value_error(validate_records, [good, dict(good)])         # повторный id
print("Проверки строгих типов пройдены")

print("Все проверки logic.py пройдены")
