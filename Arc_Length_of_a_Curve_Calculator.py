from sympy import symbols, sqrt, diff, integrate

# Define the symbol
x = symbols('x')

# Input the function of x
function_input = input("Enter the function of x for the curve (e.g., sqrt(x)): ")
f = eval(function_input)

# Input the bounds
a = float(input("Enter the lower bound: "))
b = float(input("Enter the upper bound: "))

# Compute the derivative
df = diff(f, x)

# Compute the arc length
arc_length = integrate(sqrt(1 + df**2), (x, a, b))

# Display the result
print(f"The arc length of the curve is: {arc_length}")
