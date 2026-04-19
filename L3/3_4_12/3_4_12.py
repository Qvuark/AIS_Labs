def is_palindrome(word: str) -> bool:
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left  += 1
        right -= 1
    return True


word = input("Введіть слово: ")
if is_palindrome(word):
    print(f"«{word}» є паліндромом.")
else:
    print(f"«{word}» не є паліндромом.")