import numpy as np
import matplotlib.pyplot as plt

N = 12
K = int(input("Введіть кількість елементів K: "))
L = int(input(f"Введіть нижню межу L (< {N}): "))

rng = np.random.default_rng(seed=42)
arr = rng.uniform(L, N, K)

x_min, x_max = arr.min(), arr.max()
arr_norm = (arr - x_min) / (x_max - x_min)

print(f"Початковий масив:     {np.round(arr, 3)}")
print(f"Нормалізований масив: {np.round(arr_norm, 3)}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.bar(range(K), arr, color='steelblue')
ax1.set_title(f"Початковий масив (діапазон [{L}, {N}])")
ax1.set_xlabel("Індекс")
ax1.set_ylabel("Значення")

ax2.bar(range(K), arr_norm, color='tomato')
ax2.set_title("Нормалізований масив (діапазон [0, 1])")
ax2.set_xlabel("Індекс")
ax2.set_ylabel("Значення")

plt.tight_layout()
plt.savefig("4_8_12.png", dpi=150)
print("Графік збережено: 4_8_12.png")
plt.show()