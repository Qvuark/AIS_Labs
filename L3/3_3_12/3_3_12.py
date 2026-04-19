def unique_words(sentence: str) -> list:
    words = sentence.split()
    seen = []
    for w in words:
        if w not in seen:
            seen.append(w)
    return seen


sentence = input("Введіть речення: ")
print(f"Унікальні слова: {unique_words(sentence)}")