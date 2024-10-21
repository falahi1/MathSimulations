import numpy as np
import matplotlib.pyplot as plt

def riemann_sum(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    dx = (b - a) / n
    return sum(y[:-1]) * dx

# Define the function
f = lambda x: x**2

# Input the bounds and number of rectangles
a = float(input("Enter the lower limit of integration: "))
b = float(input("Enter the upper limit of integration: "))
n = int(input("Enter the number of rectangles: "))

# Compute the Riemann sum
area = riemann_sum(f, a, b, n)

# Display the result
print(f"The Riemann sum is: {area}")
