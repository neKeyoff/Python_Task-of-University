a = int(input("Введите произвольное число "))
b = int(input("Введите пограничное число "))
while a == b:
    print("Введите разные числа ")
    a = input("Введите произвольное число ")
    b = input("Введите пограничное число ")
    if a != b:
        break
n = b
if a < b:
    print("Произвольное число меньше пограничного.")
    print(a, " < ", b)
elif a > b and a < n:
    print("Произвольное число больше пограничного.")
    print(a, " > ", b)
elif a >= n:
    print("Произвольное число больше пограничного в три раза.")
    print(a, " > ", n)