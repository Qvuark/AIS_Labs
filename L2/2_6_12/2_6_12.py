
def ivan_answer(possible: set, question: set) -> tuple:
    intersect = possible & question
    remaining = possible - question
    if len(intersect) > len(remaining):
        return "Так", intersect
    else:
        return "Ні", remaining


n = int(input())
possible = set(range(1, n + 1))

while True:
    line = input().strip()
    if line == "Все":
        print(*sorted(possible))
        break
    question = set(map(int, line.split()))
    answer, possible = ivan_answer(possible, question)
    print(answer)