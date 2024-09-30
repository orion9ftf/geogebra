import numpy as np

"""
El código calculará automáticamente los coeficientes
de las ecuaciones cuadrática y cúbica, y también calculará
las intersecciones y raíces para la función cúbica.
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
X_quad = np.vstack([x**2, x, np.ones(len(x))]).T
coeficientes_quad = np.linalg.lstsq(X_quad, y, rcond=None)[0]
a_quad, b_quad, c_quad = coeficientes_quad

# Crear la matriz de diseño para el ajuste cúbico
X_cubic = np.vstack([x**3, x**2, x, np.ones(len(x))]).T
coeficientes_cubic = np.linalg.lstsq(X_cubic, y, rcond=None)[0]
a_cubic, b_cubic, c_cubic, d_cubic = coeficientes_cubic

# Intersección con el eje y (donde x = 0)
interseccion_y_quad = c_quad
interseccion_y_cubic = d_cubic

# Calcular las raíces de la ecuación cuadrática ax^2 + bx + c = 0
discriminante_quad = b_quad**2 - 4*a_quad*c_quad
if discriminante_quad >= 0:
    raiz1_quad = (-b_quad + np.sqrt(discriminante_quad)) / (2*a_quad)
    raiz2_quad = (-b_quad - np.sqrt(discriminante_quad)) / (2*a_quad)
else:
    raiz1_quad = raiz2_quad = None

# Para la ecuación cúbica, se deben encontrar las raíces usando numpy
def encontrar_raices_cubicas(a, b, c, d):
    """Encuentra las raíces de una ecuación cúbica ax^3 + bx^2 + cx + d = 0"""
    coefs = [a, b, c, d]
    raices = np.roots(coefs)
    return raices

raices_cubic = encontrar_raices_cubicas(a_cubic, b_cubic, c_cubic, d_cubic)

print("\nAjuste polinómico cuadrático:")
print(f"Coeficientes: a = {a_quad:.2f}, b = {b_quad:.2f}, c = {c_quad:.2f}")
print(f"\nIntersección con el eje y (cuando x = 0): {interseccion_y_quad:.2f}")
if raiz1_quad is not None and raiz2_quad is not None:
    print(f"Raíces de la ecuación cuadrática: {raiz1_quad:.2f} y {raiz2_quad:.2f}")
else:
    print("La ecuación cuadrática no tiene raíces reales.")

print("\nAjuste polinómico cúbico:")
print(f"Coeficientes: a = {a_cubic:.2f}, b = {b_cubic:.2f}, c = {c_cubic:.2f}, d = {d_cubic:.2f}")
print(f"Intersección (interseca) con el eje y (cuando x = 0): {interseccion_y_cubic:.2f}")
print("\nRaíces de la ecuación cúbica:")
for raiz in raices_cubic:
    print(f"Resueve: {raiz:.2f}")
