import numpy as np
import matplotlib.pyplot as plt

def lagrange_basis(x, xi, i):
    n = len(xi)
    result = 1.0

    for j in range(n):
        if j != i:
           result *= (x - xi[j]) / (xi[i] - xi[j])
    return result

def interpolation_lagrange(xi, yi, x):
    return sum(yi[i] * lagrange_basis(x, xi, i) for i in range(len(xi)))

xi = [0, 1, 2, 3]
yi = [1, 3, 2, 5]

x_vals = np.linspace(-0.2, 3.2, 300)
y_vals = [interpolation_lagrange(xi, yi, x) for x in x_vals]

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, color='purple', label='P(x)', linewidth=2)
plt.scatter(xi, yi, color='pink', zorder=5, s=80, label='Position of interpolation')
plt.legend()
plt.axhline(0, color='blue', linewidth=1)
plt.axvline(0, color='red', linewidth=1)
plt.grid(True, alpha=0.3)
plt.show()
