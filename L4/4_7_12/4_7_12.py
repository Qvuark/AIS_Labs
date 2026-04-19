import numpy as np

N = 12 
K = int(input("Введіть розмір матриці K: "))
# Шаховий порядок: (i+j) % 2 == 1 → N, інакше → 0 (щоб [0,0]=0, [0,1]=N)
i_idx, j_idx = np.indices((K, K))
matrix = np.where((i_idx + j_idx) % 2 == 1, N, 0)

print(matrix)