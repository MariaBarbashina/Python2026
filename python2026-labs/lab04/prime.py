# Лабораторная работа 4. Дополнительное задание: проверка простоты
# Перебираем делители, пока divisor * divisor <= n — порядка sqrt(n) проверок.

n = int(input("Целое число n (не меньше 2): "))

if n < 2:
    print("Ошибка: n должно быть не меньше 2")
else:
    is_prime = True
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        print(f"{n} — простое число")
    else:
        print(f"{n} — составное число (делится на {divisor})")
