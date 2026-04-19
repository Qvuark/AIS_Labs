def rle_encode(s: str) -> str:
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(f"{s[i - 1]}{count}")
            count = 1
    result.append(f"{s[-1]}{count}")
    return "".join(result)


def rle_decode(s: str) -> str:
    result = []
    i = 0
    while i < len(s):
        ch = s[i]
        i += 1
        num = []
        while i < len(s) and s[i].isdigit():
            num.append(s[i])
            i += 1
        result.append(ch * int("".join(num)))
    return "".join(result)


s = input("Введіть рядок: ")
encoded = rle_encode(s)
decoded = rle_decode(encoded)

print(f"Закодований: {encoded}")
print(f"Декодований: {decoded}")