VOWELS = set("аеєиіїоуюяАЕЄИІЇОУЮЯaeiouAEIOU")
CONSONANTS = set("бвгґджзйклмнпрстфхцчшщьБВГҐДЖЗЙКЛМНПРСТФХЦЧШЩЬbcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")


def letter_stats(text: str) -> tuple[float, float]:
    letters = [ch for ch in text if ch in VOWELS or ch in CONSONANTS]
    if not letters:
        return 0.0, 0.0
    v = sum(1 for ch in letters if ch in VOWELS)
    c = len(letters) - v
    return v / len(letters) * 100, c / len(letters) * 100


text = input("Введіть текст: ")
vowel_pct, cons_pct = letter_stats(text)
print(f"Голосні:    {vowel_pct:.1f}%")
print(f"Приголосні: {cons_pct:.1f}%")