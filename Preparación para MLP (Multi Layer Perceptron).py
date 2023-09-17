import sympy as sp

# Define la variable simbólica
x = sp.symbols('x')

# Define la función de la que deseas calcular el gradiente
# En este ejemplo, usaremos f(x) = x^2
f = x**2

# Calcula el gradiente de la función
gradiente = sp.diff(f, x)

# Imprime el resultado
print("Función original:", f)
print("Gradiente:", gradiente)
