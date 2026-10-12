# Лабораторная работа 11. Дополнительное задание:
# выбор источника профиля (сеть или локальный пример) и общий вывод профиля.

import json
import socket
from pathlib import Path
from urllib.error import HTTPError, URLError

from fetch_profile import fetch_profile

SAMPLE_PATH = Path(__file__).resolve().parent / "profile_sample.json"


def load_sample_profile(path=SAMPLE_PATH):
    """Прочитать учебный локальный профиль через json.load."""
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict) or not isinstance(data.get("login"), str):
        raise ValueError("Файл не похож на профиль пользователя")
    return data


def print_profile(data, source):
    """Общая функция вывода профиля для обоих источников.

    Отсутствующие значения (null / None) выводятся как «не указано»,
    выдуманные данные не подставляются.
    """
    print(f"Источник: {source}")
    for key in ("login", "id", "name", "public_repos", "followers"):
        if key in data:
            value = data[key]
            if value is None:
                value = "не указано"
            print(f"  {key}: {value}")


def main():
    print("Источник профиля:")
    print("  1 — сеть (GitHub API)")
    print("  2 — локальный пример profile_sample.json")
    choice = input("Ваш выбор: ").strip()

    try:
        if choice == "1":
            data = fetch_profile(input("Логин GitHub: "))
            print_profile(data, "сеть, GitHub API")
        elif choice == "2":
            data = load_sample_profile()
            print_profile(data, "учебные локальные данные")
        else:
            print("Неизвестный пункт меню")
    except HTTPError as error:
        print(f"Сервер вернул HTTP {error.code}")
    except (URLError, TimeoutError, socket.timeout):
        print("Не удалось получить ответ по сети")
    except FileNotFoundError:
        print(f"Файл {SAMPLE_PATH.name} не найден")
    except (ValueError, UnicodeError) as error:
        print(f"Ошибка данных: {error}")
    except OSError as error:
        print(f"Ошибка доступа: {error}")


if __name__ == "__main__":
    main()
