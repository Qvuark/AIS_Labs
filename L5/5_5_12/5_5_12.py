import pandas as pd
import random

# Використовуємо DataFrame з оцінками як приклад
K = int(input("Кількість студентів (рядків): "))

random.seed(0)
df = pd.DataFrame({
    "Нейронні мережі":[random.randint(60, 100) for _ in range(K)],
    "СШІ": [random.randint(60, 100) for _ in range(K)],
    "Математика": [random.randint(60, 100) for _ in range(K)],
}, index=[f"Студент {i+1}" for i in range(K)])

k = int(input("Перші K рядків: "))
l = int(input("Останні L рядків: "))

print(f"\nПерші {k} рядки:")
print(df.head(k))

print(f"\nОстанні {l} рядки:")
print(df.tail(l))