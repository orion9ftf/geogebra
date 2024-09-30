import numpy as np

"""
El código calculará automáticamente los coeficientes
a, b y c de la ecuación cuadrática y = ax^2 + bx + c
y también calculará las intersecciones con el eje y y las raíces.
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

# Crear la matriz de diseño para el ajuste cuadrático
X = np.vstack([x**2, x, np.ones(len(x))]).T

# Resolver el sistema de ecuaciones para obtener los coeficientes a, b y c
coeficientes = np.linalg.lstsq(X, y, rcond=None)[0]
a, b, c = coeficientes

# Intersección con el eje y (donde x = 0)
interseccion_y = c

# Calcular las raíces de la ecuación cuadrática ax^2 + bx + c = 0
discriminante = b**2 - 4*a*c
if discriminante >= 0:
    raiz1 = (-b + np.sqrt(discriminante)) / (2*a)
    raiz2 = (-b - np.sqrt(discriminante)) / (2*a)
else:
    raiz1 = raiz2 = None

print("El valor del ajuste polinómico cuadrático es: a = %.2f, b = %.2f, c = %.2f" % (a, b, c))
print("Intersección con el eje y (cuando x = 0): %.2f" % interseccion_y)
if raiz1 is not None and raiz2 is not None:
    print("Raíces de la ecuación cuadrática: %.2f y %.2f" % (raiz1, raiz2))
else:
    print("La ecuación cuadrática no tiene raíces reales.")
