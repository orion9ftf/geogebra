import math
from scipy.optimize import fsolve

def f(x):
    return 83.1 / (1 + 8.9 * math.exp(-0.312 * x)) + 96.3 - 48.6 * math.log(x)

# Valor inicial
x0 = 10  # Asegúrate de que x0 sea positivo y suficientemente grande

# Usar fsolve para encontrar la raíz
sol = fsolve(f, x0)
print(f"La solución es aproximadamente x = {sol[0]}")
