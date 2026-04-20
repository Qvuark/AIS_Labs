import pandas as pd

prices = pd.Series(
    [29.99, 149.50, 9.99, 74.00, 5.49],
    index=["Кава", "Навушники", "Зошит", "Клавіатура", "Ручка"]
)

print("Series цін:")
print(prices)

label = input("\nВведіть мітку товару: ")
print(f"За міткою '{label}': {prices[label]}")

idx = int(input("Введіть числовий індекс (0-4): "))
print(f"За індексом {idx}: {prices.iloc[idx]}")