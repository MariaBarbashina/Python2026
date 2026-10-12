# Лабораторная работа 8. Автоматические проверки модуля collections_lab.py

from collections_lab import (PRINT_ORDERS, all_topics, common_topics,
                             make_record_and_pair, sorted_totals,
                             titles_in_category, totals_by_category,
                             word_counts)

# ---------- Задание 1. Частоты слов ----------
assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}
assert word_counts("!!!") == {}
assert word_counts("") == {}
assert word_counts("  Да, да; ДА!  нет.") == {"да": 3, "нет": 1}
print("Проверки word_counts пройдены")

# ---------- Задание 2. Учебные интересы ----------
first = ["python", "sql", "python"]
second = ["sql", "git"]
assert common_topics(first, second) == ["sql"]
assert all_topics(first, second) == ["git", "python", "sql"]
assert common_topics([], second) == []
assert all_topics([], second) == ["git", "sql"]
assert all_topics(first, []) == ["python", "sql"]
assert common_topics(["a"], ["b"]) == []
print("Проверки тем пройдены")

# ---------- Задание 3. Запись и пара ----------
record, pair = make_record_and_pair()
assert record == {"title": "Python", "hours": 6, "completed": False}
assert pair == ("Python", 6)
title, hours = pair
assert title == "Python" and hours == 6
print("Проверки записи и пары пройдены")

# ---------- Индивидуальный вариант: общий набор ----------
records = [
    {"title": "A", "category": "основное", "amount": 4},
    {"title": "B", "category": "дополнительное", "amount": 2},
    {"title": "C", "category": "основное", "amount": 3},
]
records_copy = [record.copy() for record in records]

assert totals_by_category(records) == {"основное": 7, "дополнительное": 2}
assert titles_in_category(records, "основное") == ["A", "C"]
assert titles_in_category(records, "нет") == []
assert totals_by_category([]) == {}
assert titles_in_category([], "основное") == []
assert records == records_copy, "исходные записи не должны меняться"
print("Проверки общего набора пройдены")

# ---------- Индивидуальный вариант 10: печатные заказы ----------
orders_copy = [order.copy() for order in PRINT_ORDERS]
assert len(PRINT_ORDERS) >= 5
assert totals_by_category(PRINT_ORDERS) == {
    "переплёт": 135,
    "цветная печать": 150,
    "чёрно-белая печать": 140,
}
assert titles_in_category(PRINT_ORDERS, "переплёт") == [
    "Курсовая работа", "Дипломная работа"]
assert titles_in_category(PRINT_ORDERS, "цветная печать") == [
    "Рекламные буклеты", "Афиши для концерта"]
assert titles_in_category(PRINT_ORDERS, "ламинирование") == []
assert PRINT_ORDERS == orders_copy, "записи варианта не должны меняться"
print("Проверки варианта 10 пройдены")

# ---------- Дополнительное задание: сортировка пар ----------
assert sorted_totals(records) == [("основное", 7), ("дополнительное", 2)]
assert sorted_totals(PRINT_ORDERS) == [
    ("цветная печать", 150),
    ("чёрно-белая печать", 140),
    ("переплёт", 135),
]
equal_totals = [
    {"title": "X", "category": "б", "amount": 5},
    {"title": "Y", "category": "а", "amount": 5},
    {"title": "Z", "category": "в", "amount": 9},
]
assert sorted_totals(equal_totals) == [("в", 9), ("а", 5), ("б", 5)]
assert sorted_totals([]) == []
print("Проверки sorted_totals пройдены")

print("Все проверки пройдены")
