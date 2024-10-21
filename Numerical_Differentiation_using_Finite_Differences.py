import numpy as np

def finite_difference(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

# Define the function
f = lambda x: np.sin(x)

# Input the point at which to differentiate
x = float(input("Enter the x value: "))

# Compute the derivative using finite differences
df = finite_difference(f, x)

# Display the result
print(f"The derivative of the function at x = {x} is: {df}")
