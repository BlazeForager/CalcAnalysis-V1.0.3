"""
Python Calculus Calculator
--------------------------
Features:
- Symbolic differentiation
- Symbolic integration (indefinite and definite)
- Limit computation
- Series expansion (Taylor series)
- Numeric evaluation of symbolic expressions

Dependencies:
- sympy

Install with:
    pip install sympy
"""

import sympy as sp

class CalculusCalculator:
    def __init__(self):
        self.x, self.y, self.z = sp.symbols('x y z')

    def differentiate(self, expr, var=None, order=1):
        if var is None:
            var = self.x
        return sp.diff(expr, var, order)

    def integrate(self, expr, var=None, lower=None, upper=None):
        if var is None:
            var = self.x
        if lower is not None and upper is not None:
            return sp.integrate(expr, (var, lower, upper))
        return sp.integrate(expr, var)

    def limit(self, expr, var, point, direction="+"):
        return sp.limit(expr, var, point, dir=direction)

    def taylor(self, expr, var=None, point=0, order=6):
        if var is None:
            var = self.x
        return sp.series(expr, var, point, order)

    def evaluate(self, expr, substitutions):
        return expr.subs(substitutions).evalf()
      
if __name__ == "__main__":
    calc = CalculusCalculator()
    x = calc.x

    # Get single expression from user input
    try:
        print("\n--- Input Format Guide ---")
        print("1. Variables: x, y, z")
        print("2. Operators: + (add), - (sub), * (mul), / (div), ** (power)")
        print("   Note: Multiplication must be explicit (e.g., 2*x, not 2x)")
        print("3. Functions: sin(), cos(), tan(), exp(), log(), sqrt()")
        print("4. Constants: pi, E")
        print("Example: sin(x)**2 + 2*x - exp(y)")
        print("--------------------------")
        expr_input = input("Expression: ")
        test_expressions = [sp.sympify(expr_input)]
    except sp.SympifyError:
         print("Invalid expression.")
         test_expressions = []

    for expr in test_expressions:
        print("\nExpression:", expr)
        print("Derivative:", calc.differentiate(expr))
        print("Second Derivative:", calc.differentiate(expr, order=2))
        print("Indefinite Integral:", calc.integrate(expr))
        print("Definite Integral [0, 1]:", calc.integrate(expr, x, 0, 1))
        print("Limit as x -> 0:", calc.limit(sp.sin(x)/x, x, 0))
        print("Taylor Series:", calc.taylor(expr, x, 0, 5))
        print("Numeric Evaluation at x=1:", calc.evaluate(expr, {x: 1}))