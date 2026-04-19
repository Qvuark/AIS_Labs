def most_frequent_from_set(s: str, symbols: set) -> list:
    freq = {ch: s.count(ch) for ch in symbols if ch in s}
    if not freq:
        return []
    max_freq = max(freq.values())
    return [ch for ch, cnt in freq.items() if cnt == max_freq]


s = input("Введіть рядок: ")
raw = input("Введіть символи множини (без пробілів): ")
symbols = set(raw)

result = most_frequent_from_set(s, symbols)
if result:
    print(f"Найчастіші символи з множини: {result}")
else:
    print("Жоден символ із множини не зустрічається в рядку.")