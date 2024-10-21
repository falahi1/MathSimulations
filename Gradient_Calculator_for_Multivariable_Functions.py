from sympy import symbols, Matrix

# Define the symbols
x, y = symbols('x y')

# Input function from user
function_input = input("Enter a multivariable function (e.g., x**2 + y**2): ")
f = eval(function_input)

# Compute the gradient
gradient = Matrix([f]).jacobian([x, y])

# Display the result
print(f"The gradient of {f} is: {gradient}")
