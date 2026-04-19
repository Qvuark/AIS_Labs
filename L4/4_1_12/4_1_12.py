import numpy as np

M = int(input("Введіть M (кількість рядків): "))
N = int(input("Введіть N (кількість стовпців): "))

matrix = np.full((M, N), 0.5)
np.fill_diagonal(matrix, -1.0)

print(repr(matrix))