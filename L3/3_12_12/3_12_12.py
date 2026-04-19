import re


def censor(text: str, forbidden: list[str]) -> str:
    for word in forbidden:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        text = pattern.sub("[ЦЕНЗУРА]", text)
    return text


text = input("Введіть текст: ")
raw  = input("Введіть заборонені слова через кому: ")
forbidden = [w.strip() for w in raw.split(",") if w.strip()]

print(censor(text, forbidden))