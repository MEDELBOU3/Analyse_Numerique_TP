import numpy as np

def LU_decomposition(A):
    A = np.array(A, dtype=float)
    n = A.shape[0]
    U = np.zeros((n, n))
    L = np.eye(n)

    for k in range(n):
        #U
        for j in range(k, n):
            U[k, j] = A[k, j] - sum(L[k, s] * U[s, k] for s in range(k))
        #L
        for i in range(k+1, n):
            L[i, k] = (A[i, k] - sum(L[i, s] * U[s, k] for s in range(k))) / U[k, k]
    return L, U

def slove_LU(L, U, b):
    b = np.array(b, dtype=float)
    n = len(b)
    x = np.zeros(n)
    y = np.zeros(n)

    #L y = b
    for i in range(n):
        y[i] = b[i] - sum(L[i, j] * y[j] for j in range(i+1, n))
    #U x = y
    for i in range(n):
        x[i] = (b[i] - sum(U[i, j] * x[j] for j in range(i+1, n))) / U[i, i] 
    return x

A = [[2, 1, 1], [-3, -1, 2], [-2, 1, 2]]
b = [8, -7, 1]

L, U = LU_decomposition(A)
solution = slove_LU(L, U, b)
print("Solution est : ", solution)