import sympy as sp
from interval import Interval
from compute_bounds import compute_bounds
from affine_form import AffineForm

x_int = Interval(10, 20)
y_int = Interval(4, 8)
x_int = x_int.standardize()
y_int = y_int.standardize()
x_affine = AffineForm.from_interval(x_int)
y_affine = AffineForm.from_interval(y_int)

x, y = sp.symbols('x y')
x0 = x_affine.center
y0 = y_affine.center
f = (-x*x  + 30 * x)/ (-y*y + 12 * y)
order = 3





