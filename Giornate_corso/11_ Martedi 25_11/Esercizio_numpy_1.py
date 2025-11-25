import numpy as np

# 1. Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace
arr = np.linspace(0, 1, 12)
print("Array 1D da linspace (12 valori tra 0 e 1):")
print(arr)
print("-" * 40)

# 2. Cambia la forma dell'array a una matrice 3x4
mat1 = arr.reshape(3, 4)
print("Matrice 3x4 ottenuta con reshape:")
print(mat1)
print("-" * 40)

# 3. Genera una matrice 3x4 di numeri casuali tra 0 e 1
mat2 = np.random.rand(3, 4)   # rand genera valori in [0, 1)
print("Matrice 3x4 di numeri casuali tra 0 e 1:")
print(mat2)
print("-" * 40)

# 4. Calcola e stampa la somma degli elementi di entrambe le matrici
somma_mat1 = mat1.sum()
somma_mat2 = mat2.sum()

print("Somma elementi matrice 1 (linspace):", somma_mat1)
print("Somma elementi matrice 2 (random):  ", somma_mat2)

print("Somma totale elementi di entrambe le matrici:",
      somma_mat1 + somma_mat2)
