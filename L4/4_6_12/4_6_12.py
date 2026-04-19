import numpy as np

N = 12 
# Ромбоподібний патерн: Manhattan distance від центру (3,3) == 3
matrix = np.zeros((7, 7), dtype=int)
i_idx, j_idx = np.indices((7, 7))
mask = np.abs(i_idx - 3) + np.abs(j_idx - 3) == 3
matrix[mask] = N

print(matrix)