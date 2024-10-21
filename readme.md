# MathSimulations

This repository contains a collection of Python scripts designed to perform a wide variety of calculus-related tasks, ranging from differentiation and integration to numerical methods and solving systems of equations. Each script is interactive, allowing you to input functions, variables, and parameters dynamically.

## Table of Contents
1. **[Derivative Calculator](#derivative-calculator)**
2. **[Partial Derivative Calculator](#partial-derivative-calculator)**
3. **[Integration Calculator (Definite and Indefinite)](#integration-calculator)**
4. **[Numerical Integration using Trapezoidal Rule](#numerical-integration-using-trapezoidal-rule)**
5. **[Simpson's Rule for Numerical Integration](#simpsons-rule-for-numerical-integration)**
6. **[Fourier Series Expansion Calculator](#fourier-series-expansion-calculator)**
7. **[Newton-Raphson Method for Root Finding](#newton-raphson-method-for-root-finding)**
8. **[Gradient Calculator (for Multivariable Functions)](#gradient-calculator)**
9. **[Jacobian Matrix Calculator](#jacobian-matrix-calculator)**
10. **[Lagrange Interpolation Calculator](#lagrange-interpolation-calculator)**
11. **[Numerical Differentiation using Finite Differences](#numerical-differentiation-using-finite-differences)**
12. **[Riemann Sum Calculator](#riemann-sum-calculator)**
13. **[Euler’s Method for Solving ODEs](#eulers-method-for-solving-differential-equations)**
14. **[Runge-Kutta Method for Solving ODEs](#runge-kutta-method-for-solving-differential-equations)**
15. **[Multivariable Chain Rule Calculator](#multivariable-chain-rule-calculator)**
16. **[Double and Triple Integral Calculator](#double-and-triple-integral-calculator)**
17. **[Arc Length of a Curve Calculator](#arc-length-of-a-curve-calculator)**
18. **[Surface Area Under a Parametric Curve](#surface-area-under-a-parametric-curve)**
19. **[Partial Fraction Decomposition](#partial-fraction-decomposition)**
20. **[Gauss-Seidel Method for Solving Systems of Equations](#gauss-seidel-method-for-solving-systems-of-equations)**

---

## Scripts and Usage

### 1. Derivative Calculator
**File**: `derivative_calculator.py`  
This script calculates the derivative of a function with respect to a variable. The user inputs the function, and the script outputs its derivative.  
**Usage**:
```bash
python derivative_calculator.py
```

---


### 2. Partial Derivative Calculator
**File**: `partial_derivative_calculator.py`  
This script calculates the partial derivatives of multivariable functions. The user inputs the function, and the script computes the partial derivatives with respect to each variable.  
**Usage**:
```bash
python partial_derivative_calculator.py
```

### 3. Integration Calculator (Definite and Indefinite)
**File**: `integration_calculator.py`  
This script performs both definite and indefinite integration on user-defined functions.
**Usage**:
```bash
python integration_calculator.py
```

### 4. Numerical Integration using Trapezoidal Rule
**File**: `trapezoidal_integration.py`  
This script approximates the integral of a function using the Trapezoidal Rule.
**Usage**:
```bash
python trapezoidal_integration.py
```

### 5. Simpson's Rule for Numerical Integration
**File**: `simpsons_rule.py`
This script performs numerical integration using Simpson's Rule for more accurate results.
**Usage**:
```bash
python simpsons_rule.py
```

### 6. Fourier Series Expansion Calculator
**File**: fourier_series_calculator.py
This script calculates the Fourier series expansion of a given periodic function.
**Usage**:
```bash
python fourier_series_calculator.py
```

### 7. Newton-Raphson Method for Root Finding
**File**: newton_raphson.py
This script uses the Newton-Raphson method to find the root of a function.
**Usage**:
```bash
python newton_raphson.py
```

### 8. Gradient Calculator (for Multivariable Functions)
**File**: gradient_calculator.py
This script calculates the gradient of a multivariable function.
**Usage**:
```bash
python gradient_calculator.py
```

### 9. Jacobian Matrix Calculator
**File**: jacobian_matrix_calculator.py
This script computes the Jacobian matrix of a set of multivariable functions.
**Usage**:
```bash
python jacobian_matrix_calculator.py
```

### 10. Lagrange Interpolation Calculator
**File**: lagrange_interpolation.py
This script performs Lagrange interpolation for polynomial approximation.
**Usage**:
```bash
python lagrange_interpolation.py
```

### 11. Numerical Differentiation using Finite Differences
**File**: finite_difference.py
This script approximates the derivative of a function using finite difference methods.
**Usage**:
```bash
python finite_difference.py
```

### 12. Riemann Sum Calculator
**File**: riemann_sum.py
This script computes the Riemann sum to approximate the area under a curve.
**Usage**:
```bash
python riemann_sum.py
```

### 13. Euler’s Method for Solving ODEs
**File**: eulers_method.py
This script solves ordinary differential equations using Euler’s method.
**Usage**:
```bash
python eulers_method.py
```

### 14. Runge-Kutta Method for Solving ODEs
**File**: runge_kutta.py
This script uses the fourth-order Runge-Kutta method to solve ordinary differential equations.
**Usage**:
```bash
python runge_kutta.py
```

### 15. Multivariable Chain Rule Calculator
**File**: multivariable_chain_rule.py
This script calculates the derivative of multivariable functions using the chain rule.
**Usage**:
```bash
python multivariable_chain_rule.py
```

### 16. Double and Triple Integral Calculator
**File**: double_triple_integral.py
This script computes double or triple integrals over a specified region.
**Usage**:
```bash
python double_triple_integral.py
```

### 17. Arc Length of a Curve Calculator
**File**: arc_length_calculator.py
This script computes the arc length of a curve between two points.
**Usage**:
```bash
python arc_length_calculator.py
```

### 18. Surface Area Under a Parametric Curve
**File**: parametric_surface_area.py
This script calculates the surface area under a parametric curve.
**Usage**:
```bash
python parametric_surface_area.py
```

### 19. Partial Fraction Decomposition
**File**: partial_fraction_decomposition.py
This script performs partial fraction decomposition for a rational function.
**Usage**:
```bash
python partial_fraction_decomposition.py
```

### 20. Gauss-Seidel Method for Solving Systems of Equations
**File**: gauss_seidel.py
This script solves systems of linear equations using the Gauss-Seidel iterative method.
**Usage**:
``` bash
python gauss_seidel.py
```

---

## How to Use
### **1**. Setup
```bash
pip install -r requirements.txt
```
### **2**. Clone the repository:
```bash
git clone https://github.com/YourUsername/MathSimulations.git
```
### **2**. Navigate to the project directory:
```bash
cd MathSimulations
```
### **3**. Run any script by invoking Python:
```bash
python <script_name>.py
```

---

## Future Plans
This repository will continue to grow with more calculus-related features such as:

- Solving systems of differential equations
- Advanced numerical methods for real-world engineering problems
- Numerical solutions for partial differential equations (PDEs)
- Implementations of advanced calculus concepts like Green's Theorem and Divergence Theorem
- Applications in fluid dynamics, aerospace, and structural mechanics
