import pandas as pd

data = {
    "Нейронні мережі": [85, 92, 78, 95, 88, 74],
    "СШІ": [90, 87, 83, 91, 76, 89],
}
students = [f"Студент {i+1}" for i in range(6)]
df = pd.DataFrame(data, index=students)

print("Таблиця оцінок:")
print(df)

print("\nСередній бал по дисциплінах:")
print(df.mean().round(2))