import numpy as np

"""
El código calculará automáticamente la pendiente 
m y la intersección b, y te dará la ecuación de la recta en forma 
y = 𝑚𝑥 + b
y=mx+b
"""

# Puntos dados
puntos = np.array([
    (1, 9867),
    (2, 9575),
    (3, 9102),
    (4, 9009),
    (5, 8956),
    (6, 8307),
    (7, 7802)
])

# Separar los valores de x e y
x = puntos[:, 0]
y = puntos[:, 1]

# Calcular las sumas necesarias
n = len(puntos)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_x2 = np.sum(x**2)
sum_xy = np.sum(x * y)

# Calcular la pendiente (m) y la intersección (b)
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
b = (sum_y - m * sum_x) / n

print("El valor de realizar el ajuste polinimico lineal es: %.2f, %.2f" % (m, b))

# Crear la matriz de diseño para el ajuste cuadrático
X = np.vstack([x**2, x, np.ones(len(x))]).T

# Resolver el sistema de ecuaciones para obtener los coeficientes a, b y c
coeficientes = np.linalg.lstsq(X, y, rcond=None)[0]
a, b, c = coeficientes

print("El valor del ajuste polinómico cuadrático es: a = %.2f, b = %.2f, c = %.2f" % (a, b, c))

