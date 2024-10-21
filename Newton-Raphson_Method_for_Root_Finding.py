import math

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    raise ValueError("Root not found within tolerance.")

# Define the function and its derivative
f = lambda x: x**3 - x - 1
df = lambda x: 3*x**2 - 1

# Input the initial guess
x0 = float(input("Enter the initial guess: "))

# Find the root using Newton-Raphson method
root = newton_raphson(f, df, x0)

# Display the result
print(f"The root of the function is: {root}")
