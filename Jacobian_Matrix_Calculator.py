from sympy import symbols, Matrix

# Define the symbols
x, y = symbols('x y')

# Input the functions
f1_input = input("Enter the first function (e.g., x**2 + y): ")
f2_input = input("Enter the second function (e.g., x*y): ")

# Define the function vector
F = Matrix([eval(f1_input), eval(f2_input)])

# Compute the Jacobian matrix
J = F.jacobian([x, y])

# Display the result
print(f"The Jacobian matrix is: {J}")
