from sympy import symbols, apart

# Define the symbol
x = symbols('x')

# Input the rational function
function_input = input("Enter a rational function (e.g., (x**2 + 2*x + 1) / (x**3 + x)): ")
f = eval(function_input)

# Perform partial fraction decomposition
decomposed = apart(f)

# Display the result
print(f"The partial fraction decomposition of {f} is: {decomposed}")
