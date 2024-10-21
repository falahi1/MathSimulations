import numpy as np


def gauss_seidel(A, b, x0, tol=1e-10, max_iter=100):
    n = len(b)
    x = x0.copy()

    for k in range(max_iter):
        x_new = np.zeros_like(x)

        for i in range(n):
            sum1 = np.dot(A[i, :i], x_new[:i])
            sum2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - sum1 - sum2) / A[i, i]

        if np.linalg.norm(x_new - x, np.inf) < tol:
            return x_new

        x = x_new

    raise ValueError("Gauss-Seidel method did not converge")


# Input the coefficient matrix and the constants vector
A = np.array([[4, 1, 2], [3, 5, 1], [1, 1, 3]], dtype=float)
b = np.array([4, 7, 3], dtype=float)
x0 = np.zeros_like(b)

# Solve the system using Gauss-Seidel method
solution = gauss_seidel(A, b, x0)

# Display the result
print(f"The solution to the system is: {solution}")
