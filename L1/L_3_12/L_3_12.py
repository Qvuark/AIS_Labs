
def compute_term(k, n, x):
    sign = (-1) ** (k + 1)
    numerator = x ** (2 * k - 1)
    factor1 = n - k + 1
    exp = sign * k
    base = x + sign * k

    if factor1 == 0:
        raise ValueError(f"(n−k+1) = 0 при k = {k}")
    if abs(base) < 1e-12:
        raise ValueError(
            f"Основа (x {'+ ' if sign > 0 else '− '}{k}) = 0 при k = {k}"
        )

    return sign * numerator / (factor1 * (base ** exp))


def sum_for(n, x):
    try:
        total = 0.0
        for k in range(1, n + 1):
            total += compute_term(k, n, x)
        return True, total
    except (ValueError, ZeroDivisionError, OverflowError) as e:
        return False, str(e)


def sum_while(n, x):
    try:
        total = 0.0
        k = 1
        while k <= n:
            total += compute_term(k, n, x)
            k += 1
        return True, total
    except (ValueError, ZeroDivisionError, OverflowError) as e:
        return False, str(e)


def sum_recursive(n, x):
    def _recurse(k):
        if k > n:
            return 0.0
        return compute_term(k, n, x) + _recurse(k + 1)

    try:
        return True, _recurse(1)
    except (ValueError, ZeroDivisionError, OverflowError) as e:
        return False, str(e)
    except RecursionError:
        return False, "n завелике для рекурсії (межа Python ~1000 рівнів)"


def main():
    print("=== Сума ряду — Варіант 12, Завдання 3 ===\n")

    while True:
        try:
            n = int(input("Введіть n (кількість членів, n ∈ ℕ): "))
            if n < 1:
                raise ValueError
            break
        except ValueError:
            print("Помилка: n повинно бути натуральним числом.\n")

    while True:
        try:
            x = float(input("Введіть x (x ∈ ℝ): "))
            break
        except ValueError:
            print("Помилка: x повинно бути числом.\n")

    print()

    implementations = [
        ("for      ", sum_for),
        ("while    ", sum_while),
        ("рекурсія ", sum_recursive),
    ]

    for label, func in implementations:
        ok, value = func(n, x)
        if ok:
            print(f"  [{label}] Сума = {value:.10f}")
        else:
            print(f"  [{label}] Помилка: {value}")


if __name__ == "__main__":
    main()