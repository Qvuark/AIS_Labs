import numpy as np

raw1 = input("Введіть елементи першого масиву через пробіл: ")
raw2 = input("Введіть індекси через пробіл: ")

a = np.array(list(map(float, raw1.split())))
idx = np.array(list(map(int, raw2.split())))

print(f"Перший масив: {a}")
print(f"Індекси:      {idx}")
print(f"Результат:    {a[idx]}")