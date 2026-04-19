import random

def fill_random(n: int, a: int, b: int) -> list:
    return [random.randint(a, b) for _ in range(n)]


n = int(input("Кількість елементів n: "))
a = int(input("Нижня межа a: "))
b = int(input("Верхня межа b: "))

lst = fill_random(n, a, b)
print(f"Список: {lst}")