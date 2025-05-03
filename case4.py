import sympy as sp
import numpy as np
from interval import Interval
from affine_form import AffineForm
from compute_bounds import compute_bounds
from taylor_expansion import taylor_expansion

# INPUT DATA
x_interval_4 = Interval(10, 20)
y_interval_4 = Interval(4, 8)
x_interval_4 = x_interval_4.standardize()
y_interval_4 = y_interval_4.standardize()
x_affine_4 = AffineForm.from_interval(x_interval_4)
y_affine_4 = AffineForm.from_interval(y_interval_4)

# TAYLOR EXPANSION FOR FUNCTION F(X, Y) = (-X^2+30*X + 10)/(-X^2+6*Y)
x4, y4 = sp.symbols("x4 y4")
f4 = (((2/3)*x4*x4 - x4 - (1/60))/(x4*x4+-0.12*y4))
x40, y40 = x_affine_4.center, y_affine_4.center
_, H = taylor_expansion(f4, [x4, y4], [x40, y40], 4)

# COMPUTE BOUNDS
f_lower_4, f_upper_4 = compute_bounds([x_affine_4, y_affine_4], H)
f_lower_4, f_upper_4 = 1.5 * f_lower_4, 1.5 * f_upper_4
print(f"Function in interval: [{round(f_lower_4,2)}, {round(f_upper_4, 2)}]")

