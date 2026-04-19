def get_negatives_loop(a: list) -> list:
    result = []
    for x in a:
        if x < 0:
            result.append(x)
    return result


def get_negatives_comp(a: list) -> list:
    return [x for x in a if x < 0]


raw = input("Введіть числа через пробіл: ")
a = list(map(int, raw.split()))

print(f"Вхідний список:       {a}")
print(f"Від'ємні (цикл):      {get_negatives_loop(a)}")
print(f"Від'ємні (генератор): {get_negatives_comp(a)}")