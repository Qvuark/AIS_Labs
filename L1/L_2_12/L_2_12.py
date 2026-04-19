import math

def compute_y(x):
    x_rad = math.radians(x)
    if x < 3:
        subfunc = "lg( cos(2x) / (x − 0.5) )"
        if abs(x - 0.5) < 1e-12:
            return None, subfunc, "Знаменник (x − 0.5) дорівнює нулю"
        cos2x = math.cos(2 * x_rad)
        fraction = cos2x / (x - 0.5)
        if fraction <= 0:
            return None, subfunc, f"Аргумент lg = {fraction:.6g} ≤ 0 — не визначено"

        return math.log10(fraction), subfunc, None
    elif x >= 4:
        subfunc = "ln( cos(x) / (1 + tg²(x)) )"
        cos_x = math.cos(x_rad)
        if abs(cos_x) < 1e-12:
            return None, subfunc, "cos(x) = 0 — tg(x) не визначено"

        tan_x = math.tan(x_rad)
        fraction = cos_x / (1 + tan_x ** 2)
        if fraction <= 0:
            return None, subfunc, f"cos(x) = {cos_x:.6g} < 0 — аргумент ln ≤ 0"

        return math.log(fraction), subfunc, None
    else:
        return None, "—", "Функція не визначена при 3 ≤ x < 4"


def main():
    print("=== Складна функція — Варіант 12, Завдання 2 ===\n")

    while True:
        try:
            key = float(input("Введіть ключове значення x (зупинить програму): "))
            break
        except ValueError:
            print("Помилка: введіть число.\n")
    print()
    while True:
        try:
            x = float(input("x (у градусах): "))
        except ValueError:
            print("  Помилка: введіть число.\n")
            continue

        if x == key:
            print(f"\nВведено ключове значення x = {key}. Завершення програми.")
            break

        result, subfunc, error = compute_y(x)
        print(f"  Підфункція: {subfunc}")

        if result is not None:
            print(f"  y = {result:.8f}\n")
        else:
            print(f"  Помилка: {error}\n")
if __name__ == "__main__":
    main()