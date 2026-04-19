def letter_p(num: int) -> list[str]:
    n = str(num)
    return [
        " ____ ",
        "|    \\",
        f"| {n:<2} |",
        "|____/",
        "|     ",
        "|     ",
    ]


n = int(input("Введіть n (1–9): "))
n = max(1, min(9, n))

rows = [letter_p(i) for i in range(1, n + 1)]

for row_idx in range(6):
    line = " ".join(rows[i][row_idx] for i in range(n))
    print(line)