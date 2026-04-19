import numpy as np
import matplotlib.pyplot as plt

# Складна функція варіанту 12 (x у градусах):
#   y = lg( cos(2x) / (x - 0.5) ),  при x < 3
#   y = ln( cos(x) / (1 + tg²(x)) ),  при x >= 4

def compute_branch1(x_deg):
    """x < 3: y = lg( cos(2x_rad) / (x - 0.5) )"""
    x_rad = np.radians(x_deg)
    denom = x_deg - 0.5
    with np.errstate(divide='ignore', invalid='ignore'):
        frac = np.cos(2 * x_rad) / denom
        y = np.where(frac > 0, np.log10(frac), np.nan)
    return y


def compute_branch2(x_deg):
    """x >= 4: y = ln( cos(x_rad) / (1 + tg²(x_rad)) ) = ln(cos³(x_rad))"""
    x_rad = np.radians(x_deg)
    cos_x = np.cos(x_rad)
    with np.errstate(divide='ignore', invalid='ignore'):
        frac = np.where(np.abs(cos_x) > 1e-10,
                        cos_x / (1 + np.tan(x_rad)**2),
                        np.nan)
        y = np.where(frac > 0, np.log(frac), np.nan)
    return y


# Гілка 1: x < 3 (уникаємо x = 0.5)
x1 = np.linspace(-90, 2.99, 1000)
x1 = x1[np.abs(x1 - 0.5) > 0.01]
y1 = compute_branch1(x1)

# Гілка 2: x >= 4, cos(x_rad) > 0
x2 = np.linspace(4, 89, 1000)
y2 = compute_branch2(x2)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x1, y1, color='steelblue', linewidth=1.5, label='$y = \lg(\\cos(2x)/(x-0.5))$, $x < 3$')
ax.plot(x2, y2, color='tomato',    linewidth=1.5, label='$y = \ln(\\cos(x)/(1+\\mathrm{tg}^2x))$, $x \\geq 4$')

ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlabel('x (градуси)')
ax.set_ylabel('y')
ax.set_title('Графік складної функції (варіант 12)')
ax.legend()
ax.grid(True, alpha=0.3)
ax.set_ylim(-5, 5)

plt.tight_layout()
plt.savefig("4_10_12.png", dpi=150)
print("Графік збережено: 4_10_12.png")
plt.show()