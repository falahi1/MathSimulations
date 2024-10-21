import numpy as np


def simpsons_rule(f, a, b, n):
    if n % 2 == 1:
        raise ValueError("Number of intervals 'n' must be even.")

    x = np.linspace(a, b, n + 1)
    y = f(x)

    h = (b - a) / n
    integral = (h / 3) * (y[0] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-2:2]) + y[-1])
    return integral


# Define the function to integrate
f = lambda x: x ** 2 + 3 * x

# Input the bounds and number of intervals
a = float(input("Enter the lower limit of integration: "))
b = float(input("Enter the upper limit of integration: "))
n = int(input("Enter the number of intervals (must be even): "))

# Perform integration using Simpson's Rule
result = simpsons_rule(f, a, b, n)

# Display the result
print(f"The integral of the function using Simpson's Rule is: {result}")
