import sympy as sp
import numpy as np
from interval import Interval
from affine_form import AffineForm
from compute_bounds import compute_bounds



# TAYLOR EXPANSION
mu, s = sp.symbols("mu s")
mu0 = 0.7
s0 = 0.9
f = sp.sqrt(mu * s)
order = 3

# TUTAJ ZAIMPLEMENTOWAĆ AUTOMATYCZNE ROZWINIĘCIE WE WZÓR TAYLORA

# APPROXIMATE FUNCTION
mu = Interval(0.65, 0.75)
s = Interval(8, 10)
s = s.standardize()

mu_affine = AffineForm.from_interval(mu)
s_affine = AffineForm.from_interval(s)
H = np.array([[-0.421, 2.0464, -2.2656, 0.9135], 
              [0.5346, 0.6681, -0.1043, 0], 
              [-0.3819, -0.1193, 0, 0], 
              [0.1364, 0, 0, 0]])


f_lower, f_upper = compute_bounds([mu_affine, s_affine], H)

f_lower = f_lower * np.sqrt(20 * 9.81)
f_upper = f_upper * np.sqrt(20 * 9.81)

print(f"Velocity in interval: [{round(f_lower,2)}, {round(f_upper, 2)}] m/s")