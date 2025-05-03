import sympy as sp
import numpy as np
from interval import Interval
from affine_form import AffineForm
from compute_bounds import compute_bounds
from taylor_expansion import taylor_expansion

# INPUT DATA
x_interval_3 = Interval(-2, 2)
y_interval_3 = Interval(1, 3)
x_interval_3 = x_interval_3.standardize()
y_interval_3 = y_interval_3.standardize()
x_affine_3 = AffineForm.from_interval(x_interval_3)
y_affine_3 = AffineForm.from_interval(y_interval_3)

# TAYLOR EXPANSION FOR FUNCTION FROM ARTICLE F(X,Y) = X^2 + Y
x3, y3 = sp.symbols("x3 y3")
f3 = (4* x3*x3  + 3* y3)
x30, y30 = x_affine_3.center, y_affine_3.center
_, H = taylor_expansion(f3, [x3, y3], [x30, y30], 4)

# COMPUTE BOUNDS
f_lower_3, f_upper_3 = compute_bounds([x_affine_3, y_affine_3], H)
print(f"Function in interval: [{round(f_lower_3,2)}, {round(f_upper_3, 2)}]")

