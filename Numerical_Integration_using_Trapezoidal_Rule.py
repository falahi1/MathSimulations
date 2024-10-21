import numpy as np


def trapezoidal_rule(f, a, b, n):
    # Divide the interval into n subintervals
    x = np.linspace(a, b, n + 1)
    y = f(x)

    # Calculate the trapezoidal sum
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * sum(y[1:-1]) + y[-1])
    return integral


# Define the function to integrate
f = lambda x: x ** 2 + 3 * x

# Input the bounds and number of subintervals
a = float(input("Enter the lower limit of integration: "))
b = float(input("Enter the upper limit of integration: "))
n = int(input("Enter the number of subintervals: "))

# Perform integration using Trapezoidal Rule
result = trapezoidal_rule(f, a, b, n)

# Display the result
print(f"The integral of the function using Trapezoidal Rule is: {result}")
