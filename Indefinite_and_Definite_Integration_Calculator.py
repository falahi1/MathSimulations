from sympy import symbols, integrate

# Define the symbol
x = symbols('x')

# Input function from user
function_input = input("Enter a function of x (e.g., x**2 + 3*x): ")
f = eval(function_input)

# Choose type of integration
integration_type = input("Would you like indefinite or definite integration? (i/d): ")

if integration_type == 'i':
    # Perform indefinite integration
    integral = integrate(f, x)
    print(f"The indefinite integral of {f} with respect to x is: {integral}")
else:
    # Input bounds for definite integration
    a = float(input("Enter the lower limit of integration: "))
    b = float(input("Enter the upper limit of integration: "))

    # Perform definite integration
    definite_integral = integrate(f, (x, a, b))
    print(f"The definite integral of {f} from {a} to {b} is: {definite_integral}")
