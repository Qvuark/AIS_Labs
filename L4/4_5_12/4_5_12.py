import numpy as np

N = 12
K = int(input("Введіть розмір матриці K: "))

matrix = np.zeros((K, K), dtype=int)
anti_diag_idx = (np.arange(K), np.arange(K - 1, -1, -1))
matrix[anti_diag_idx] = N

print(matrix)