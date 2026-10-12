"""Дополнительное задание: окно поиска и просмотра печатных заказов (tkinter).

Используются готовые функции проекта: load_records, find_records,
sorted_records и format_record. Обработчики кнопок только вызывают их и
показывают результат. Окно не изменяет и не сохраняет data.json.
"""

import json
import tkinter as tk
from tkinter import ttk

from logic import find_records, sorted_records
from main import DATA_PATH, format_record
from storage import load_records


def load_for_window():
    """Загрузить записи. Вернуть (records, сообщение) или (None, ошибка)."""
    try:
        records = load_records(DATA_PATH)
    except FileNotFoundError:
        return [], f"Файл {DATA_PATH.name} не найден — список пуст"
    except UnicodeError:
        return None, f"Файл {DATA_PATH.name} не в кодировке UTF-8"
    except json.JSONDecodeError:
        return None, f"Файл {DATA_PATH.name} повреждён"
    except ValueError as error:
        return None, f"Ошибка данных: {error}"
    except OSError as error:
        return None, f"Ошибка доступа: {error}"
    return records, f"Загружено заказов: {len(records)}"


def create_app(root, records, message):
    """Создать виджеты окна. Вернуть словарь с переменными и обработчиками."""
    root.title("Учёт печатных заказов — поиск")
    query = tk.StringVar()
    status = tk.StringVar(value=message)

    frame = ttk.Frame(root, padding=12)
    frame.pack(fill=tk.BOTH, expand=True)

    ttk.Label(frame, text="Часть названия:").grid(row=0, column=0, sticky="w")
    entry = ttk.Entry(frame, textvariable=query, width=40)
    entry.grid(row=0, column=1, sticky="ew", padx=6)
    search_button = ttk.Button(frame, text="Найти")
    search_button.grid(row=0, column=2, padx=3)
    all_button = ttk.Button(frame, text="Показать все")
    all_button.grid(row=0, column=3, padx=3)

    listbox = tk.Listbox(frame, width=90, height=12)
    listbox.grid(row=1, column=0, columnspan=4, sticky="nsew", pady=8)
    ttk.Label(frame, textvariable=status).grid(row=2, column=0, columnspan=4, sticky="w")

    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(1, weight=1)

    def show(found):
        listbox.delete(0, tk.END)
        for record in found:
            listbox.insert(tk.END, format_record(record))

    def search():
        try:
            found = find_records(records, query.get())
        except ValueError:
            show([])
            status.set("Поисковый запрос не может быть пустым")
            return
        show(found)
        if found:
            status.set(f"Найдено заказов: {len(found)}")
        else:
            status.set(f"По запросу «{query.get().strip()}» ничего не найдено")

    def show_all():
        show(sorted_records(records))
        if records:
            status.set(f"Всего заказов: {len(records)}")
        else:
            status.set("Нет записей")

    search_button.configure(command=search)
    all_button.configure(command=show_all)
    entry.bind("<Return>", lambda event: search())
    entry.focus()

    if records:
        show_all()

    return {"query": query, "status": status, "listbox": listbox,
            "search": search, "show_all": show_all}


def main():
    root = tk.Tk()
    records, message = load_for_window()
    if records is None:
        root.title("Учёт печатных заказов — ошибка")
        ttk.Label(root, text=message, padding=20).pack()
        ttk.Button(root, text="Закрыть", command=root.destroy).pack(pady=8)
    else:
        create_app(root, records, message)
    root.mainloop()


if __name__ == "__main__":
    main()
