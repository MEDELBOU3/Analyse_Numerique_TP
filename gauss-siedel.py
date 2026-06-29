import numpy as np
import matplotlib.pyplot as plt
from jacobi2 import  max_iterations, errors
def GaussSiedel(A, b, x0, tol=1e-6, max_iter=100):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x = np.array(x0, dtype=float)
    n = len(b)

    x_satrt = np.linalg.solve(A, b)
    errs = []

    for k in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            s1 = sum(A[i, j] * x_new[j] for j in range(n) if j < i)
            s2 = sum(A[i, j] * x[j] for j in range(n) if j > i)
            x_new[i] = (b[i] - (s1+s2)) / A[i, i]
        err = np.linalg.norm(x_new - x_satrt)
        errs.append(err)

        if np.linalg.norm(x_new - x) < tol:
            x = x_new
            print(f"La convergence de methode atteint a {k+1} itterations")
            return x, k+1, errs
        x = x_new
    print(f"Le nomber maximal des iteration {k+1} atteint sans convergence.")
    return x, max_iter, errs

A = np.array(
    [
        [4, 1, 0], [1, 4, 1], [0,1, 4]
    ], dtype=float
)

b = np.array([5, 6, 5], dtype=float)
x0 = np.array([0, 0, 0], dtype=float)

solution_g, max_iteration_g, errors_g = GaussSiedel(A, b, x0)
print("La solution du system est : ", solution_g)
print("Le nombre maximal des iteration est : ", max_iteration_g)
print("Les erreurs sont : \n", errors_g)
if(max_iterations > max_iteration_g):
    print(f"iterations de == Jacobi == {max_iterations} plus grand que de == guasse == {max_iteration_g}")
elif (max_iterations < max_iteration_g):
    print(f"iterations de == Jacobi == {max_iterations} plus petit que de == guasse == {max_iteration_g}")

iterations_j = range(1, len(errors) + 1)
iterations_g = range(1, len(errors_g) + 1)
plt.figure(figsize=(8, 5))

plt.plot(iterations_g, errors_g, color='black', label='Covergence de la courbe Gauss', linewidth=2)
plt.plot(iterations_j, errors, color='green', label='Covergence de la courbe Jacobi', linewidth=1.5)
plt.scatter(iterations_g, errors_g, color='orange', zorder=5, s=60 ,label='Erreros par ietrations Gauss')
plt.scatter(iterations_j, errors, color='pink', zorder=5, s=60 ,label='Erreros par ietrations Jacobi')
plt.legend()
plt.grid(True, alpha=0.3)
plt.axhline(0, color='red', linewidth=1)
plt.axvline(0, color='blue', linewidth=1)
plt.yscale('log')
plt.show()