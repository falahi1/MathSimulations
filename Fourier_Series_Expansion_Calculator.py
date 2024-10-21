from sympy import symbols, fourier_series

# Define the symbol
x = symbols('x')

# Input function from user
function_input = input("Enter a periodic function of x (e.g., sin(x), cos(x)): ")
f = eval(function_input)

# Input the period
period = float(input("Enter the period of the function: "))

# Compute Fourier series expansion
fourier_expansion = fourier_series(f, (x, 0, period))

# Display the result
print(f"The Fourier series expansion of {f} is: {fourier_expansion.truncate(5)}")
