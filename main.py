import numpy as np
from interval import Interval




# INITIAL PARAMETERS
mu = Interval(0.65, 0.75)
s = Interval(8, 10)
g = 9.81
print(mu)

# STANDARDIZE
s_standardized = s.standardize()
print(s_standardized)
