print("--- Hernadez Dylan NC:1245 Fecha:22/10/26 ---")
import numpy as np
print("=== 1. Indexacion de un arreglo de una dimension ===")
n1245 = np.array([10, 20, 30, 40, 50])
print(n1245)
print(n1245[0])
print(n1245[3])
print(n1245[-1])
print(n1245[-2])
print("-" * 40)
print("=== 2. Indexacion de un arreglo de dos dimensiones (2D) ===")
n1245 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(n1245)
print(n1245[0, 0])
print(n1245[1, 2])
print(n1245[-1, -1])
print(n1245[-2, -2])
print("-" * 40)
print("=== 3. Indexacion de un arreglo de tres dimensiones (3D) ===")
n1245 = np.array([
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
])
print(n1245)
print(n1245[0, 0, 0])
print(n1245[1, 1, 2])
print(n1245[-1, -1, -2])
print("--- Hernadez Dylan NC:1245 Fecha:22/10/26 ---")