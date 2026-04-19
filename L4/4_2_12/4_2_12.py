import numpy as np

M = int(input("Введіть M: "))
N = int(input("Введіть N: "))

matrix = np.full((M, N), 0.5)
np.fill_diagonal(matrix, -1.0)

print("Матриця:")
print(matrix)

r1 = int(input("Рядок лівого верхнього кута: "))
c1 = int(input("Стовпець лівого верхнього кута: "))
r2 = int(input("Рядок правого нижнього кута: "))
c2 = int(input("Стовпець правого нижнього кута: "))

submatrix = matrix[r1:r2+1, c1:c2+1]
print("Підматриця:")
print(submatrix)