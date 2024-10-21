from sympy import symbols, integrate

# Define the symbols
x, y, z = symbols('x y z')

# Input the function for double or triple integration
function_input = input("Enter the function (e.g., x**2 + y**2): ")
f = eval(function_input)

# Ask if the user wants to calculate a double or triple integral
integral_type = input("Would you like to compute a double or triple integral? (d/t): ")

if integral_type == 'd':
    # Input bounds for double integral
    x_lower = float(input("Enter the lower limit for x: "))
    x_upper = float(input("Enter the upper limit for x: "))
    y_lower = float(input("Enter the lower limit for y: "))
    y_upper = float(input("Enter the upper limit for y: "))

    # Perform double integration
    double_integral = integrate(integrate(f, (y, y_lower, y_upper)), (x, x_lower, x_upper))
    print(f"The double integral is: {double_integral}")
else:
    # Input bounds for triple integral
    x_lower = float(input("Enter the lower limit for x: "))
    x_upper = float(input("Enter the upper limit for x: "))
    y_lower = float(input("Enter the lower limit for y: "))
    y_upper = float(input("Enter the upper limit for y: "))
    z_lower = float(input("Enter the lower limit for z: "))
    z_upper = float(input("Enter the upper limit for z: "))

    # Perform triple integration
    triple_integral = integrate(integrate(integrate(f, (z, z_lower, z_upper)), (y, y_lower, y_upper)),
                                (x, x_lower, x_upper))
    print(f"The triple integral is: {triple_integral}")
