import sympy as sp
import numpy as np
from interval import Interval
from affine_form import AffineForm
from compute_bounds import compute_bounds
from taylor_expansion import taylor_expansion

# INPUT DATA
x_interval_2 = Interval(10, 20)
y_interval_2 = Interval(4, 8)
x_interval_2 = x_interval_2.standardize()
y_interval_2 = y_interval_2.standardize()
x_affine_2 = AffineForm.from_interval(x_interval_2)
y_affine_2 = AffineForm.from_interval(y_interval_2)

# TAYLOR EXPANSION FOR FUNCTION F(X,Y) = (-X^2 + 30*X)/(-Y^2+12*Y)
x2, y2 = sp.symbols("x2 y2")
f2 = (-(2/3)*x2*x2  +   x2)/ (-(2/3)*y2*y2 + y2)
x20, y20 = x_affine_2.center, y_affine_2.center
_, H = taylor_expansion(f2, [x2, y2], [x20, y20], 4)

# COMPUTE BOUNDS
f_lower, f_upper = compute_bounds([x_affine_2, y_affine_2], H)
f_lower, f_upper = 6.25 * f_lower, 6.25 * f_upper
print(f"Function in interval: [{round(f_lower,2)}, {round(f_upper, 2)}]")




