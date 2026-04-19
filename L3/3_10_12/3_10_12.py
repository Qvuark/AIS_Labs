def reverse_words(sentence: str) -> str:
    return " ".join(word[::-1] for word in sentence.split())


sentence = input("Введіть речення: ")
print(reverse_words(sentence))