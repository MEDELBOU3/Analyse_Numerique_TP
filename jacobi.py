import numpy as np
import matplotlib.pyplot as plt

def Jacobi(A, b, x0, tol=1e-6, max_iter= 100):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x = np.array(x0, dtype=float)
    n = len(b)

    x_start = np.linalg.solve(A, b)
    errs = []

    for k in range(max_iter):
        x_new = np.zeros(n)
        for i in range(n):
            s = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s)/A[i,i]

        err = np.linalg.norm(x_new - x_start)
        errs.append(err)

        if np.linalg.norm(x_new - x) < tol:
            x = x_new
            print(f"La convergence atteint a {k+1} iterration.")
            return x, k+1, errs
        
        x = x_new

    print(f"Le nombre max des iterration {k+1} atteint sans convergence.")
    return x, max_iter, errs

A = np.array([
    [4, 1, 0],
    [1, 4, 1],
    [0, 1, 4]
],  dtype=float)


b = np.array([5, 6, 5], dtype=float)
x0 = np.array([0, 0, 0], dtype=float)

solution, max_iteration, erros = Jacobi(A, b, x0)

print("La solution du system est ===================================== : \n", solution)
print("Le nombre maximal des iterations est : =============================== \n", max_iteration)
print("Les errors sont : \n", erros)

iteration = range(1, len(erros) + 1)
plt.figure(figsize=(8, 5))
plt.plot(iteration, erros, color='red', label='Convergence de la coube', linewidth=2)
plt.scatter(iteration, erros, color='blue', zorder=9, s=20, label='Erreurs par iterations')
plt.legend()
plt.yscale('log')
plt.grid(True, alpha=0.3)
plt.show()