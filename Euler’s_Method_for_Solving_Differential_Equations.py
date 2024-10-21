import numpy as np
import matplotlib.pyplot as plt


def eulers_method(f, y0, t0, tn, h):
    t_values = np.arange(t0, tn + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0

    for i in range(1, len(t_values)):
        y_values[i] = y_values[i - 1] + h * f(t_values[i - 1], y_values[i - 1])

    return t_values, y_values


# Define the ODE y' = f(t, y)
f = lambda t, y: t - y

# Initial conditions
y0 = float(input("Enter the initial value of y: "))
t0 = float(input("Enter the initial value of t: "))
tn = float(input("Enter the value of t to solve up to: "))
h = float(input("Enter the step size (h): "))

# Solve the ODE using Euler's method
t_values, y_values = eulers_method(f, y0, t0, tn, h)

# Plot the result
plt.plot(t_values, y_values, 'b-', label="Approximate solution (Euler's method)")
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
