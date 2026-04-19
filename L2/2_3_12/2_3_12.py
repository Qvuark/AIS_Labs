def remove_value_loop(lst: list, n) -> list:
    result = []
    for x in lst:
        if x != n:
            result.append(x)
    return result


def remove_value_comp(lst: list, n) -> list:
    return [x for x in lst if x != n]


raw = input("Введіть числа через пробіл: ")
lst = list(map(int, raw.split()))
n = int(input("Число для видалення n: "))

print(f"Вхідний список:     {lst}")
print(f"Без {n} (цикл):      {remove_value_loop(lst, n)}")
print(f"Без {n} (генератор): {remove_value_comp(lst, n)}")