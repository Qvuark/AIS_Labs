import re

def get_words(s: str, separators: str) -> list[str]:
    pattern = "[" + re.escape(separators) + "]+"
    return [w for w in re.split(pattern, s) if w]


def is_real_number(word: str) -> bool:
    try:
        float(word)
        return True
    except ValueError:
        return False


s = input("Введіть рядок: ")
seps = input("Введіть символи-розділювачі (підряд, без пробілів між ними): ")

words = get_words(s, seps)
numbers = [w for w in words if is_real_number(w)]

print(f"Слова: {words}")
print(f"Десяткові записи дійсних чисел: {numbers}")
print(f"Кількість: {len(numbers)}")