def count_substring(s: str, sub: str) -> int:
    if not sub:
        return 0
    count = 0
    i = 0
    while i <= len(s) - len(sub):
        if s[i:i + len(sub)] == sub:
            count += 1
        i += 1
    return count


s   = input("Введіть рядок: ")
sub = input("Введіть підрядок: ")
print(f"Кількість входжень '{sub}' у рядку: {count_substring(s, sub)}")