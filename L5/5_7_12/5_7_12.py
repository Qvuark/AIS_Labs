import pandas as pd

df = pd.DataFrame({
    "Товар":["Ноутбук", "Мишка", "Клавіатура", "Монітор", "Навушники", "Веб-камера"],
    "Ціна":[32999.0, 599.0, 1299.0, 8499.0, 2149.0, 1799.0],
})

print("Початкова таблиця:")
print(df.to_string(index=False))

df_sorted = df.sort_values("Ціна").reset_index(drop=True)

print("\nВідсортована за ціною (зростання):")
print(df_sorted.to_string(index=False))