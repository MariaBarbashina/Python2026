# Лабораторная работа 1. Задание 1: карточка студента

WEEKS = 4
DAYS_IN_WEEK = 7
YEARS_AHEAD = 4

last_name = input("Фамилия: ")
first_name = input("Имя: ")
group = input("Группа: ")
city = input("Город: ")
age = int(input("Возраст (полных лет, от 1 до 120): "))
favorite_subject = input("Любимый предмет: ")
study_hours = float(input("Часы подготовки в неделю: "))

full_name = f"{first_name} {last_name}"
future_age = age + YEARS_AHEAD
hours_four_weeks = study_hours * WEEKS
hours_per_day = study_hours / DAYS_IN_WEEK

print()
print("========== КАРТОЧКА СТУДЕНТА ==========")
print(f"Полное имя: {full_name}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Возраст: {age}")
print(f"Любимый предмет: {favorite_subject}")
print(f"Подготовка в неделю: {study_hours:.2f} ч")
print(f"Возраст через четыре года: {future_age}")
print(f"Подготовка за четыре недели: {hours_four_weeks:.2f} ч")
print(f"Среднее время подготовки в день: {hours_per_day:.2f} ч")
