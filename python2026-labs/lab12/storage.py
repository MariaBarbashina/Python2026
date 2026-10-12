"""Хранение данных проекта в JSON. Без консольных диалогов."""

import json
import os
from pathlib import Path

from logic import validate_records


def load_records(path):
    """Прочитать и проверить список записей из JSON-файла UTF-8.

    Исключения: FileNotFoundError — файла нет; UnicodeDecodeError —
    неверная кодировка; json.JSONDecodeError — повреждённый JSON;
    ValueError — неправильная структура; OSError — ошибка доступа.
    Файл только читается и никогда не перезаписывается.
    """
    with open(path, "r", encoding="utf-8") as file:
        records = json.load(file)
    validate_records(records)
    return records


def save_records(path, records):
    """Записать список записей в JSON (UTF-8, читаемая кириллица).

    Данные сначала пишутся во временный файл рядом, затем он заменяет
    основной. Если запись не удалась, выбрасывается OSError, а прежний
    файл остаётся без изменений.
    """
    path = Path(path)
    temp_path = path.with_name(path.name + ".tmp")
    try:
        with open(temp_path, "w", encoding="utf-8") as file:
            json.dump(records, file, ensure_ascii=False, indent=2)
            file.write("\n")
        os.replace(temp_path, path)
    except OSError:
        if temp_path.is_file():
            temp_path.unlink()
        raise
