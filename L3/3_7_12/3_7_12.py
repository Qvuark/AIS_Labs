def is_identifier(word: str) -> bool:
    if not word:
        return False
    if not (word[0].isalpha() and word[0].isascii() or word[0] == '_'):
        return False
    for ch in word[1:]:
        if not (ch.isalnum() and ch.isascii() or ch == '_'):
            return False
    return True


word = input("Введіть слово: ")
if is_identifier(word):
    print(f"«{word}» є ідентифікатором.")
else:
    print(f"«{word}» не є ідентифікатором.")