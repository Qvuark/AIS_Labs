import pandas as pd
import random

K = int(input("Введіть K (кількість студентів): "))

random.seed(42)
data = {
    "Нейронні мережі": [random.randint(60, 100) for _ in range(K)],
    "СШІ":             [random.randint(60, 100) for _ in range(K)],
}
df = pd.DataFrame(data, index=[f"Студент {i+1}" for i in range(K)])
print(df)