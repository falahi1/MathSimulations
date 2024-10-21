import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x_points, y_points, x):
    n = len(x_points)
    result = 0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# Input points
x_points = np.array([0, 1, 2, 3])
y_points = np.array([1, 2, 0, 4])

# Input x value to interpolate
x = float(input("Enter the x value to interpolate: "))

# Perform Lagrange interpolation
y = lagrange_interpolation(x_points, y_points, x)

# Display the result
print(f"The interpolated value at x = {x} is: {y}")

# Plot the interpolation
x_range = np.linspace(min(x_points), max(x_points), 100)
y_range = [lagrange_interpolation(x_points, y_points, xi) for xi in x_range]

plt.plot(x_points, y_points, 'ro', label='Data Points')
plt.plot(x_range, y_range, 'b-', label='Lagrange Polynomial')
plt.legend()
plt.show()
