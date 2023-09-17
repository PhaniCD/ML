import sympy as sp
import numpy as np

# Definir las variables simbólicas
x1, x2 = sp.symbols('x1 x2')

# Definir la función
f = 10 - sp.exp(x1**2 + x2**2)

# Calcular el gradiente
grad_x1 = sp.diff(f, x1)
grad_x2 = sp.diff(f, x2)

# Convertir la función y el gradiente en funciones de Python
f_py = sp.lambdify((x1, x2), f, 'numpy')
grad_x1_py = sp.lambdify((x1, x2), grad_x1, 'numpy')
grad_x2_py = sp.lambdify((x1, x2), grad_x2, 'numpy')

# Inicializar valores iniciales y tasa de aprendizaje
x1_val = 1.0
x2_val = 1.0
learning_rate = 0.1
iterations = 100

# Optimización utilizando el gradiente descendente
for i in range(iterations):
    gradient_x1 = grad_x1_py(x1_val, x2_val)
    gradient_x2 = grad_x2_py(x1_val, x2_val)
    x1_val -= learning_rate * gradient_x1
    x2_val -= learning_rate * gradient_x2

# Imprimir el resultado
print("Valor óptimo de x1:", x1_val)
print("Valor óptimo de x2:", x2_val)
print("Valor óptimo de la función f(x1, x2):", f_py(x1_val, x2_val))
