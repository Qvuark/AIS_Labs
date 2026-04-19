def in_intervals(x: float, intervals: list) -> bool:
    return any(a <= x <= b for a, b in intervals)


def split_by_intervals(lst: list, intervals: list) -> tuple:
    inside  = [x for x in lst if     in_intervals(x, intervals)]
    outside = [x for x in lst if not in_intervals(x, intervals)]
    return inside, outside


raw = input("Введіть дійсні числа через пробіл: ")
lst = list(map(float, raw.split()))

k = int(input("Кількість проміжків: "))
intervals = []
for i in range(k):
    ab = input(f"  Проміжок {i + 1} (a b через пробіл): ").split()
    intervals.append([float(ab[0]), float(ab[1])])

inside, outside = split_by_intervals(lst, intervals)
print(f"\nПроміжки:   {intervals}")
print(f"Входять:    {inside}")
print(f"Не входять: {outside}")