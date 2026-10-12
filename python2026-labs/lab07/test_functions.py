# Лабораторная работа 7. Автоматические проверки функций

from functions import (average, is_palindrome, normalize_text,
                       select_numbers, sum_digits)

# ---------- Базовые проверки из методички ----------
assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""
print("Базовые проверки пройдены")

# ---------- Дополнительные проверки базовых функций ----------
assert sum_digits(9) == 9
assert sum_digits(-1000) == 1
assert abs(average([1, 2]) - 1.5) < 1e-9
assert average([-3]) == -3
source = [5, 1, 3]
source_copy = source.copy()
average(source)
assert source == source_copy, "average не должна менять список"
assert normalize_text("Python") == "python"
assert normalize_text("") == ""
print("Дополнительные проверки базовых функций пройдены")

# ---------- Вариант 10: от минус порога до 0 включительно ----------
assert select_numbers([-5, 0, 2, 5], 2) == [0]           # контрольный пример
assert select_numbers([-3, -2, -1, 0, 1], 2) == [-2, -1, 0]  # пример с совпадениями
assert select_numbers([], 2) == []                       # пустой список
assert select_numbers([-3, -2], 2) == [-2]               # граница -2 входит, -3 нет
assert select_numbers([0, 1], 2) == [0]                  # граница 0 входит, 1 нет
assert select_numbers([-1, 0, 1], 0) == [0]              # порог 0: подходит только 0
assert select_numbers([5, 7, -9], 3) == []               # совпадений нет
assert select_numbers([-1, 4, -1, 0, -1], 1) == [-1, -1, 0, -1]  # повторы сохранены

numbers = [-4, -2, 0, 3, -2]
numbers_copy = numbers.copy()
result = select_numbers(numbers, 2)
assert result == [-2, 0, -2]
assert numbers == numbers_copy, "исходный список не должен меняться"
assert result is not numbers, "должен возвращаться новый список"
print("Проверки варианта 10 пройдены")

# ---------- Дополнительное задание: is_palindrome ----------
# Проверки написаны до реализации функции.
assert is_palindrome("А роза упала на лапу Азора") is True
assert is_palindrome("а    ") is True
assert is_palindrome("   ") is False
assert is_palindrome("") is False
assert is_palindrome("Python") is False
assert is_palindrome("А!") is False
print("Проверки is_palindrome пройдены")

print("Все проверки пройдены")
