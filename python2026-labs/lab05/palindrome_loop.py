# Лабораторная работа 5. Дополнительное задание: палиндром без обратного среза
# Правила те же, что в palindrome.py. Цикл обходит половину длины
# очищенной строки и сравнивает символы с двух концов.

text = input("Введите текст: ")

cleaned = text.lower().replace(" ", "")

if cleaned == "":
    print("Нет текста")
else:
    is_palindrome = True
    length = len(cleaned)
    for index in range(length // 2):
        if cleaned[index] != cleaned[length - 1 - index]:
            is_palindrome = False
            break

    if is_palindrome:
        print("Палиндром")
    else:
        print("Не палиндром")
