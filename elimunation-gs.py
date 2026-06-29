import numpy as np

def elimunationGauss(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)

    for k in range(n-1):
        pivot = k
        for i in range(k+1, n):
            if(abs(A[i, k]) > abs(A[pivot, k])):
                pivot = i

        if pivot != k:
           A[[k, pivot]] = A[[pivot, k]]
           b[[k, pivot]] = b[[pivot, k]]
        
        for i in range(k+1, n):
            m = A[i, k] / A[k, k]
            A[i, k:] -= m * A[k, k:]
            b[i] -= m*b[k]

    x = [0]*n
    for i in range(n-1, -1, -1):
        s = 0
        for j in range(i+1, n):
            s += A[i, j] * x[j]
        x[i] = (b[i] - s) / A[i, i]
    return x
    
A = [[2, 1, 1], [-3, -1, 2], [-2, 1, 2]]
b = [8, -7, 1]

solution_ga = elimunationGauss(A, b)
print("La solution du gausse est : ", solution_ga)

print("Solution par linalg : ", np.linalg.solve(A, b))
    