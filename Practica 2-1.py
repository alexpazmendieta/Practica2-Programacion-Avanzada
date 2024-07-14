import numpy as np

dimensiones = (5, 4, 3)

array_tridimensional = np.random.randint(0, 101, size=dimensiones)

min_valor = float('inf')
max_valor = float('-inf')
pos_min = None
pos_max = None

for i in range(dimensiones[0]):
    for j in range(dimensiones[1]):
        for k in range(dimensiones[2]):
            valor = array_tridimensional[i, j, k]
            if valor < min_valor:
                min_valor = valor
                pos_min = (i, j, k)
            if valor > max_valor:
                max_valor = valor
                pos_max = (i, j, k)
                
print("Array tridimensional:")
print(array_tridimensional)
print(f"Elemento más pequeño: {min_valor} en la posición {pos_min}")
print(f"Elemento más grande: {max_valor} en la posición {pos_max}")