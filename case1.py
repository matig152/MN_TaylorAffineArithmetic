import sympy as sp
import numpy as np
from interval import Interval
from affine_form import AffineForm
from compute_bounds import compute_bounds
from taylor_expansion import taylor_expansion

# INPUT DATA
mu_interval = Interval(0.65, 0.75)
s_interval = Interval(8, 10)
s_interval = s_interval.standardize()
mu_affine = AffineForm.from_interval(mu_interval)
s_affine = AffineForm.from_interval(s_interval)

# TAYLOR EXPANSION
mu, s = sp.symbols("mu s")
f1 = sp.sqrt(mu * s)
mu0, s0 = mu_affine.center, s_affine.center
_, H = taylor_expansion(f1, [mu, s], [mu0, s0], 4)

# COMPUTE BOUNDS 
f_lower, f_upper = compute_bounds([mu_affine, s_affine], H)
f_lower = f_lower * np.sqrt(20 * 9.81)
f_upper = f_upper * np.sqrt(20 * 9.81)
print(f"Velocity in interval: [{round(f_lower,2)}, {round(f_upper, 2)}] m/s")