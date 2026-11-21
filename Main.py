
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')

# Input
function = input("Enter f(x): ")
x0 = float(input("Enter starting value X0: "))

# Function and its derivative
f = sp.sympify(function)
df = sp.diff(f, x)

F = sp.lambdify(x, f, 'numpy')
DF = sp.lambdify(x, df, 'numpy')

# Newton-Raphson iterations
values = [x0]
tolerance = 0.0001

for i in range(100):
    current = values[-1]

    if abs(DF(current)) < 1e-12:
        print("Derivative is zero. Cannot continue.")
        break

    next_x = current - F(current) / DF(current)
    values.append(next_x)

    print(f"Iteration {i + 1}: x = {next_x:.6f}")

    if abs(next_x - current) < tolerance:
        break

print("\nApproximate Root:", values[-1])
print("Number of Iterations:", len(values) - 1)

# Draw graph
margin = max(1, (max(values) - min(values)) * 0.5)
a = min(values) - margin
b = max(values) + margin

X = np.linspace(a, b, 500)
Y = F(X)

plt.plot(X, Y, label="f(x)")
plt.axhline(0, color='black')
plt.scatter(values, [F(v) for v in values], color='red', label="Iterations")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Newton-Raphson Method")
plt.grid()
plt.legend()
plt.show()
