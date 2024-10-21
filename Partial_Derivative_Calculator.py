from sympy import symbols, diff

# Define the symbols for multivariable calculus
x, y = symbols('x y')

# Input function from user
function_input = input("Enter a function of x and y (e.g., x**2 + y**3): ")
f = eval(function_input)

# Partial derivatives
partial_x = diff(f, x)
partial_y = diff(f, y)

# Display the result
print(f"Partial derivative with respect to x: {partial_x}")
print(f"Partial derivative with respect to y: {partial_y}")
