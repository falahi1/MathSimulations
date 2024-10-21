from sympy import symbols, diff, integrate, pi

# Define the symbols
x, t = symbols('x t')

# Input parametric equations
x_input = input("Enter the parametric equation for x(t) (e.g., cos(t)): ")
y_input = input("Enter the parametric equation for y(t) (e.g., sin(t)): ")
x_t = eval(x_input)
y_t = eval(y_input)

# Input the bounds for the parameter t
a = float(input("Enter the lower bound of t: "))
b = float(input("Enter the upper bound of t: "))

# Compute the surface area
dx_dt = diff(x_t, t)
dy_dt = diff(y_t, t)
ds = sqrt(dx_dt**2 + dy_dt**2)
surface_area = 2 * pi * integrate(x_t * ds, (t, a, b))

# Display the result
print(f"The surface area under the parametric curve is: {surface_area}")
