import numpy as np
from interval import Interval
from affine_form import AffineForm
import sympy as sp



# INITIAL PARAMETERS
mu = Interval(0.65, 0.75)
s = Interval(8, 10)
g = 9.81
# print(mu)

# STANDARDIZE
s_standardized = s.standardize()
# print(s_standardized)


# CREATE AFFINE FORM
x = AffineForm(2, [3, 2])
y = AffineForm(1, [2, 7])
# print(x.scalar_mul(2))


# TAYLOR EXPANSION

# Define symbols
mu, s = sp.symbols("mu s")

f = sp.sqrt(mu * s)

mu0 = 0.7
s0 = 0.9

n = 3

taylor_series = 0
for i in range(n + 1):
    for j in range(n + 1 - i):
        term = (f.diff(mu, i).diff(s, j).subs({mu: mu0, s: s0}) / (sp.factorial(i) * sp.factorial(j))) * (mu - mu0)**i * (s - s0)**j
        taylor_series += term

taylor_series = sp.simplify(taylor_series)
sp.pprint(taylor_series)
