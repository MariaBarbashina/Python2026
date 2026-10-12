"""Лабораторная работа 8. Словари, множества и кортежи (вариант 10).

Вариант 10: печатные заказы, поле amount — количество страниц.
"""

PUNCTUATION = ".,!?;:"

# Записи варианта 10: печатные заказы (вымышленные данные).
PRINT_ORDERS = [
    {"title": "Курсовая работа", "category": "переплёт", "amount": 45},
    {"title": "Рекламные буклеты", "category": "цветная печать", "amount": 120},
    {"title": "Методичка по Python", "category": "чёрно-белая печать", "amount": 80},
    {"title": "Дипломная работа", "category": "переплёт", "amount": 90},
    {"title": "Афиши для концерта", "category": "цветная печать", "amount": 30},
    {"title": "Конспект лекций", "category": "чёрно-белая печать", "amount": 60},
]


# ---------- Задание 1. Частоты слов ----------

def word_counts(text):
    """Вернуть словарь «слово → количество».

    Слова приводятся к нижнему регистру, с их краёв удаляются символы
    .,!?;: , пустые результаты пропускаются.
    """
    counts = {}
    for word in text.lower().split():
        cleaned = word.strip(PUNCTUATION)
        if cleaned == "":
            continue
        counts[cleaned] = counts.get(cleaned, 0) + 1
    return counts


def print_word_counts(counts):
    """Вывести пары «слово: количество» в алфавитном порядке."""
    if len(counts) == 0:
        print("Нет слов")
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")


# ---------- Задание 2. Учебные интересы ----------

def common_topics(first, second):
    """Вернуть отсортированный список тем, общих для двух списков."""
    return sorted(set(first) & set(second))


def all_topics(first, second):
    """Вернуть отсортированный список всех уникальных тем двух списков."""
    return sorted(set(first) | set(second))


# ---------- Задание 3. Запись и пара ----------

def make_record_and_pair():
    """Создать запись-словарь, изменить её и вернуть (запись, кортеж)."""
    record = {"title": "Python", "hours": 4}
    record["hours"] = 6             # изменение существующего ключа
    record["completed"] = False     # добавление нового ключа
    pair = (record["title"], record["hours"])
    return record, pair


# ---------- Индивидуальный вариант 10 ----------

def totals_by_category(records):
    """Вернуть словарь «категория → сумма amount». Записи не изменяются."""
    totals = {}
    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + record["amount"]
    return totals


def titles_in_category(records, category):
    """Вернуть названия записей указанной категории в исходном порядке."""
    titles = []
    for record in records:
        if record["category"] == category:
            titles.append(record["title"])
    return titles


def total_sort_key(pair):
    """Ключ сортировки пары (category, total): сначала большая сумма,
    при равенстве — категория по алфавиту."""
    category, total = pair
    return (-total, category)


def sorted_totals(records):
    """Дополнительное задание: вернуть список пар (category, total),
    отсортированных по убыванию суммы, а при равенстве — по названию."""
    totals = totals_by_category(records)
    return sorted(totals.items(), key=total_sort_key)


def main():
    print("=== Задание 1. Частоты слов ===")
    text = input("Введите текст: ")
    print_word_counts(word_counts(text))

    print()
    print("=== Задание 2. Учебные интересы ===")
    first = ["python", "sql", "python"]
    second = ["sql", "git"]
    print(f"Первый список: {first}")
    print(f"Второй список: {second}")
    print(f"Общие темы: {common_topics(first, second)}")
    print(f"Все темы: {all_topics(first, second)}")

    print()
    print("=== Задание 3. Запись и пара ===")
    record, pair = make_record_and_pair()
    print(f"Запись: {record}")
    title, hours = pair
    print(f"Кортеж: {pair}")
    print(f"Распаковка: title = {title}, hours = {hours}")

    print()
    print("=== Вариант 10. Печатные заказы (страницы) ===")
    for order in PRINT_ORDERS:
        print(f"{order['title']} | {order['category']} | {order['amount']} стр.")
    print()
    print("Сводка по категориям:")
    totals = totals_by_category(PRINT_ORDERS)
    for category in sorted(totals):
        print(f"{category}: {totals[category]} стр.")

    print()
    print("Категории по убыванию страниц:")
    for category, total in sorted_totals(PRINT_ORDERS):
        print(f"{category}: {total} стр.")

    print()
    category = input("Категория для поиска: ").strip().lower()
    print(f"Заказы категории «{category}»: "
          f"{titles_in_category(PRINT_ORDERS, category)}")


if __name__ == "__main__":
    main()
