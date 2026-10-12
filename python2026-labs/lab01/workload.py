# Лабораторная работа 1. Задание 2: учебная нагрузка

MINUTES_IN_HOUR = 60
WEEKS = 4

first_subject = input("Название первого предмета: ")
first_count = int(input("Количество занятий по первому предмету в неделю: "))
first_duration = int(input("Продолжительность одного занятия, мин: "))

second_subject = input("Название второго предмета: ")
second_count = int(input("Количество занятий по второму предмету в неделю: "))
second_duration = int(input("Продолжительность одного занятия, мин: "))

available_hours = float(input("Доступное время на неделю, ч: "))

first_minutes = first_count * first_duration
second_minutes = second_count * second_duration
total_minutes = first_minutes + second_minutes
total_hours = total_minutes / MINUTES_IN_HOUR
free_hours = available_hours - total_hours
four_weeks_hours = total_hours * WEEKS

print()
print("========== УЧЕБНАЯ НАГРУЗКА ==========")
print(f"{first_subject}: {first_minutes} мин в неделю")
print(f"{second_subject}: {second_minutes} мин в неделю")
print(f"Общая нагрузка: {total_minutes} мин ({total_hours:.2f} ч)")
print(f"Остаток свободного времени: {free_hours:.2f} ч")
print(f"Нагрузка за четыре недели: {four_weeks_hours:.2f} ч")
