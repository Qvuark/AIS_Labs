import pandas as pd

K = int(input("Введіть K (кількість мов): "))

languages = ["Python", "Java", "C#", "C++", "JavaScript","TypeScript", "Go", "Rust", "Kotlin", "Swift"]

series = pd.Series(languages[:K], index=range(1, K + 1))
print(series)