import numpy as np
import matplotlib.pyplot as plt


def runge_kutta(f, y0, t0, tn, h):
    t_values = np.arange(t0, tn + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0

    for i in range(1, len(t_values)):
        t = t_values[i - 1]
        y = y_values[i - 1]

        k1 = h * f(t, y)
        k2 = h * f(t + h / 2, y + k1 / 2)
        k3 = h * f(t + h / 2, y + k2 / 2)
        k4 = h * f(t + h, y + k3)

        y_values[i] = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return t_values, y_values


# Define the ODE y' = f(t, y)
f = lambda t, y: t - y

# Initial conditions
y0 = float(input("Enter the initial value of y: "))
t0 = float(input("Enter the initial value of t: "))
tn = float(input("Enter the value of t to solve up to: "))
h = float(input("Enter the step size (h): "))

# Solve the ODE using Runge-Kutta method
t_values, y_values = runge_kutta(f, y0, t0, tn, h)

# Plot the result
plt.plot(t_values, y_values, 'g-', label="Approximate solution (Runge-Kutta method)")
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
