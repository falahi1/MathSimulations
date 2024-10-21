from sympy import symbols, diff

# Define the symbols
x, y, z = symbols('x y z')

# Input function from user
function_input = input("Enter a function of x, y, z (e.g., x**2 * y + z): ")
f = eval(function_input)

# Input chain rule variables
variable = input("Differentiate with respect to which variable? (x, y, z): ")

# Compute the derivative using the chain rule
if variable == 'x':
    derivative = diff(f, x)
elif variable == 'y':
    derivative = diff(f, y)
elif variable == 'z':
    derivative = diff(f, z)

# Display the result
print(f"The derivative of {f} with respect to {variable} is: {derivative}")
