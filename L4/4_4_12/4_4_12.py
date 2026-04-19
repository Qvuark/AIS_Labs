import numpy as np

raw = input("Введіть елементи масиву через пробіл: ")
a   = np.array(list(map(float, raw.split())))
val = float(input("Введіть порогове значення: "))

print(f"Масив:                {a}")
print(f"Елементи > {val}: {a[a > val]}")
print(f"Елементи < {val}: {a[a < val]}")