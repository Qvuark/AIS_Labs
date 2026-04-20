import pandas as pd

df = pd.read_csv("education.csv")

print(f"Кількість рядків:   {df.shape[0]}")
print(f"Кількість стовпців: {df.shape[1]}")
print(f"\nПерші 3 рядки:")
print(df.head(3))