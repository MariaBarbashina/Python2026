# Лабораторная работа 2. Задание 1: перевод времени

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600

total_seconds = int(input("Количество секунд (целое, не меньше 0): "))

hours = total_seconds // SECONDS_IN_HOUR
minutes = total_seconds % SECONDS_IN_HOUR // SECONDS_IN_MINUTE
seconds = total_seconds % SECONDS_IN_MINUTE

print(f"{hours} ч {minutes} мин {seconds} с")
