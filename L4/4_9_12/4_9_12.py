import numpy as np
import matplotlib.pyplot as plt

K = int(input("Введіть кількість рядків K: "))
L = int(input("Введіть кількість стовпців L: "))

rng = np.random.default_rng(seed=0)
img = rng.integers(0, 256, size=(K, L)).astype(float)

neighbors = (
    img[0:-2, 0:-2] + img[0:-2, 1:-1] + img[0:-2, 2:] +
    img[1:-1, 0:-2] + img[1:-1, 1:-1] + img[1:-1, 2:] +
    img[2:,   0:-2] + img[2:,   1:-1] + img[2:,   2:]
)
smoothed = img.copy()
smoothed[1:-1, 1:-1] = neighbors / 9.0

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.imshow(img,      cmap='gray', vmin=0, vmax=255)
ax1.set_title("Початкове зображення")
ax2.imshow(smoothed, cmap='gray', vmin=0, vmax=255)
ax2.set_title("Після згладжування")
plt.tight_layout()
plt.savefig("4_9_12.png", dpi=150)
print("Графік збережено: 4_9_12.png")
plt.show()