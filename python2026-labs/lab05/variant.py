# Лабораторная работа 5. Индивидуальный вариант 10
# Отбираем слова, которые начинаются и заканчиваются одной и той же буквой.

PUNCTUATION = ".,!?;:"

text = input("Введите строку: ")

count = 0
for word in text.split():
    cleaned = word.strip(PUNCTUATION).lower()
    if cleaned == "":
        continue
    # к первому символу обращаемся только после пропуска пустых слов
    if cleaned.endswith(cleaned[0]):
        print(cleaned)
        count += 1

if count == 0:
    print("Нет совпадений")
print(f"Количество: {count}")
