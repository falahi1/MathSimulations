from sympy import symbols, diff

# Define the symbol
x = symbols('x')

# Input function from user
function_input = input("Enter a function of x (e.g., x**3 + 2*x + 1): ")
f = eval(function_input)

# Calculate the derivative
derivative = diff(f, x)

# Display the result
print(f"The derivative of {f} with respect to x is: {derivative}")
