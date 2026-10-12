# Итоговый проект. Автоматические проверки storage.py во временной папке

import json
from pathlib import Path
from tempfile import TemporaryDirectory

from logic import add_record, delete_record, set_completed
from storage import load_records, save_records


def expect_error(error_type, path):
    """Проверить, что load_records(path) выбрасывает error_type."""
    try:
        load_records(path)
    except error_type:
        pass
    else:
        assert False, f"Ошибка {error_type.__name__} не обнаружена"


with TemporaryDirectory() as directory:
    folder = Path(directory)
    path = folder / "data.json"

    # ---------- Сохранение и повторная загрузка ----------
    records = []
    add_record(records, "  Курсовая работа  ", "переплёт", 45)
    add_record(records, "Рекламные буклеты", "цветная печать", 120)
    add_record(records, "Рекламные буклеты", "цветная печать", 0)   # повтор названия
    set_completed(records, 2, True)
    delete_record(records, 1)
    save_records(path, records)
    restored = load_records(path)
    assert restored == records, "после перезагрузки данные отличаются"
    assert restored[0] == {"id": 2, "title": "Рекламные буклеты",
                           "category": "цветная печать", "amount": 120,
                           "completed": True}
    assert type(restored[0]["completed"]) is bool
    assert "Рекламные" in path.read_text(encoding="utf-8")   # кириллица читаема
    assert not (folder / "data.json.tmp").exists()          # временный файл удалён
    print("Проверки сохранения и повторной загрузки пройдены")

    # Пустой список
    save_records(path, [])
    assert load_records(path) == []
    path.write_text("[]", encoding="utf-8")
    assert load_records(path) == []

    # Дополнительные ключи сохраняются без обработки
    extra = [{"id": 7, "title": "А", "category": "Б", "amount": 1,
              "completed": False, "comment": "срочно"}]
    save_records(path, extra)
    assert load_records(path) == extra
    print("Проверки пустого списка и дополнительных ключей пройдены")

    # ---------- Ошибки загрузки ----------
    expect_error(FileNotFoundError, folder / "missing.json")

    path.write_text('[{"id": 1, "title": "А",', encoding="utf-8")
    expect_error(json.JSONDecodeError, path)

    path.write_text("", encoding="utf-8")
    expect_error(json.JSONDecodeError, path)

    path.write_text('[{"id": 1, "title": "А", "category": "Б", "amount": 1, "completed": false},'
                    ' {"id": 1, "title": "В", "category": "Б", "amount": 2, "completed": true}]',
                    encoding="utf-8")
    expect_error(ValueError, path)          # повторный id

    path.write_text('{"id": 1}', encoding="utf-8")
    expect_error(ValueError, path)          # корень не список

    path.write_text('[{"id": 1, "title": "А", "category": "Б", "amount": true, "completed": false}]',
                    encoding="utf-8")
    expect_error(ValueError, path)          # amount = true

    path.write_bytes('[{"id": 1, "title": "Заказ", "category": "Б", "amount": 1, "completed": false}]'
                     .encode("cp1251"))
    expect_error(UnicodeError, path)        # неверная кодировка

    # Загрузка не изменяет повреждённый файл
    broken = b'[{"id": 1, "title": '
    path.write_bytes(broken)
    expect_error(json.JSONDecodeError, path)
    assert path.read_bytes() == broken
    print("Проверки ошибок загрузки пройдены")

    # ---------- Ошибка сохранения ----------
    good = [{"id": 1, "title": "А", "category": "Б", "amount": 1, "completed": False}]
    save_records(path, good)
    original = path.read_bytes()
    (folder / "data.json.tmp").mkdir()      # временный файл нельзя создать
    try:
        save_records(path, [])
    except OSError:
        pass
    else:
        assert False, "Ошибка записи не обнаружена"
    assert path.read_bytes() == original, "прежний файл повреждён при ошибке записи"

    try:
        save_records(folder / "нет_папки" / "data.json", good)
    except OSError:
        pass
    else:
        assert False, "Ошибка записи не обнаружена"
    print("Проверки ошибок сохранения пройдены")

print("Все проверки storage.py пройдены")
