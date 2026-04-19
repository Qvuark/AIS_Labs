def count_digits(s: str) -> int:
    count = 0
    for ch in s:
        if ch.isdigit():
            count += 1
    return count


s = input("Введіть рядок: ")
print(f"Кількість цифр: {count_digits(s)}")