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

# Define expansion order
n = 3

# Compute Taylor expansion around (mu0, s0)
taylor_series = 0
for i in range(n + 1):
    for j in range(n + 1 - i):
        deriv = f.diff(mu, i).diff(s, j).subs({mu: mu0, s: s0})
        term = deriv / (sp.factorial(i) * sp.factorial(j)) * (mu - mu0)**i * (s - s0)**j
        taylor_series += term

taylor_series = sp.expand(taylor_series)
print(taylor_series)


# Extract coefficients into matrix H
H = sp.Matrix.zeros(n + 1, n + 1)
for i in range(n + 1):
    for j in range(n + 1 - i):
        coeff = taylor_series.coeff((mu - mu0)**i * (s - s0)**j)
        H[i, j] = coeff

# Display the result
sp.pprint(H)

# APPROXIMATE FUNCTION
mu = Interval(0.65, 0.75)
s = Interval(8, 10)
s = s.standardize()

mu_affine = AffineForm.from_interval(mu)
s_affine = AffineForm.from_interval(s)
H = np.array(H)


f_lower, f_upper = compute_bounds([mu_affine, s_affine], H)

f_lower = f_lower * np.sqrt(20 * 9.81)
f_upper = f_upper * np.sqrt(20 * 9.81)

print(f"Velocity in interval: [{round(f_lower,2)}, {round(f_upper, 2)}] m/s")