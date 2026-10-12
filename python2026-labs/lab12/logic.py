"""Логика проекта «Учёт печатных заказов» (вариант 10).

Запись заказа — словарь с обязательными полями:
    id        — положительное целое, уникальное в списке;
    title     — название заказа, непустая строка;
    category  — категория (вид печати), непустая строка;
    amount    — количество страниц, целое не меньше 0;
    completed — True, если заказ напечатан.

Модуль не выполняет ввод-вывод в консоль и не работает с файлами.
Контракты функций, изменяющих список, указаны в их документации.
"""

REQUIRED_KEYS = ("id", "title", "category", "amount", "completed")


def validate_records(records):
    """Проверить весь набор записей. Список не изменяется.

    При нарушении формата выбрасывает ValueError с пояснением.
    Дополнительные ключи в записях допустимы.
    """
    if type(records) is not list:
        raise ValueError("Корень JSON должен быть списком записей")

    seen_ids = set()
    for index, record in enumerate(records):
        place = f"Запись №{index + 1}"
        if type(record) is not dict:
            raise ValueError(f"{place}: ожидался объект JSON")

        for key in REQUIRED_KEYS:
            if key not in record:
                raise ValueError(f"{place}: нет обязательного поля «{key}»")

        record_id = record["id"]
        # type(...) is int отсекает True/False, которые проходят isinstance
        if type(record_id) is not int or record_id <= 0:
            raise ValueError(f"{place}: id должен быть положительным целым")
        if record_id in seen_ids:
            raise ValueError(f"{place}: повторный id {record_id}")
        seen_ids.add(record_id)

        for key in ("title", "category"):
            value = record[key]
            if type(value) is not str or value.strip() == "":
                raise ValueError(f"{place}: поле «{key}» должно быть непустой строкой")

        amount = record["amount"]
        if type(amount) is not int or amount < 0:
            raise ValueError(f"{place}: amount должен быть целым числом не меньше 0")

        if type(record["completed"]) is not bool:
            raise ValueError(f"{place}: completed должен быть true или false")


def clean_text(value, field_name):
    """Вернуть строку без пробелов по краям; пустую строку отклонить."""
    if type(value) is not str:
        raise ValueError(f"{field_name}: ожидалась строка")
    cleaned = value.strip()
    if cleaned == "":
        raise ValueError(f"{field_name}: значение не может быть пустым")
    return cleaned


def check_amount(amount):
    """Проверить количество страниц: целое не меньше 0, не bool."""
    if type(amount) is not int or amount < 0:
        raise ValueError("Количество страниц должно быть целым числом не меньше 0")


def next_id(records):
    """Вернуть id для новой записи: максимум существующих плюс 1, для [] — 1."""
    if len(records) == 0:
        return 1
    return max(record["id"] for record in records) + 1


def add_record(records, title, category, amount):
    """Добавить новый заказ в конец списка records (список ИЗМЕНЯЕТСЯ).

    Название и категория очищаются от пробелов по краям, статус — False.
    Возвращает добавленную запись. При некорректных данных выбрасывает
    ValueError, и список не меняется.
    """
    clean_title = clean_text(title, "Название заказа")
    clean_category = clean_text(category, "Категория заказа")
    check_amount(amount)
    record = {
        "id": next_id(records),
        "title": clean_title,
        "category": clean_category,
        "amount": amount,
        "completed": False,
    }
    records.append(record)
    return record


def get_record(records, record_id):
    """Вернуть запись с указанным id или None. Список не изменяется."""
    for record in records:
        if record["id"] == record_id:
            return record
    return None


def record_id_key(record):
    """Ключ сортировки записей по id."""
    return record["id"]


def sorted_records(records):
    """Вернуть новый список записей по возрастанию id. Исходный не меняется."""
    return sorted(records, key=record_id_key)


def find_records(records, query):
    """Вернуть записи, в названии которых есть подстрока query, без учёта
    регистра, по возрастанию id. Список не изменяется.

    Пустой (после strip) запрос — ValueError.
    """
    cleaned_query = query.strip().lower()
    if cleaned_query == "":
        raise ValueError("Поисковый запрос не может быть пустым")
    found = []
    for record in sorted_records(records):
        if cleaned_query in record["title"].lower():
            found.append(record)
    return found


def set_completed(records, record_id, completed):
    """Установить статус заказа с указанным id (запись ИЗМЕНЯЕТСЯ).

    Возвращает True при успехе и False, если id не найден (данные не
    меняются). completed должен быть bool, иначе ValueError.
    """
    if type(completed) is not bool:
        raise ValueError("Статус должен быть True или False")
    record = get_record(records, record_id)
    if record is None:
        return False
    record["completed"] = completed
    return True


def delete_record(records, record_id):
    """Удалить заказ с указанным id из списка (список ИЗМЕНЯЕТСЯ).

    Возвращает True при успехе и False, если id не найден (список не
    меняется). Идентификаторы оставшихся записей не перенумеровываются.
    """
    for index, record in enumerate(records):
        if record["id"] == record_id:
            records.pop(index)
            return True
    return False


def statistics(records):
    """Вернуть статистику по текущему списку. Список не изменяется.

    Словарь: total — число записей, completed — напечатано,
    not_completed — не напечатано, amount_total — сумма страниц,
    by_category — словарь «категория → сумма страниц»; категории
    сравниваются точно после удаления пробелов по краям.
    """
    completed_count = 0
    amount_total = 0
    by_category = {}
    for record in records:
        if record["completed"]:
            completed_count += 1
        amount_total += record["amount"]
        category = record["category"].strip()
        by_category[category] = by_category.get(category, 0) + record["amount"]
    return {
        "total": len(records),
        "completed": completed_count,
        "not_completed": len(records) - completed_count,
        "amount_total": amount_total,
        "by_category": by_category,
    }
