def insert_before(lst: list, value, index: int) -> list:
    return lst[:index] + [value] + lst[index:]


raw = input("Введіть числа через пробіл: ")
lst = list(map(int, raw.split()))
value = int(input("Число для вставки: "))
index = int(input("Індекс (перед яким вставити): "))

print(f"Результат: {insert_before(lst, value, index)}")