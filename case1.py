import sympy as sp
from interval import Interval


# INITIAL PARAMETERS
mu = Interval(0.65, 0.75)
s = Interval(8, 10)
g = 9.81
s_standardized = s.standardize()

# TAYLOR EXPANSION
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
print(taylor_series)