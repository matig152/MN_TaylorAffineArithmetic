import numpy as np
from interval import Interval
from affine_form import AffineForm



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
print(x.scalar_mul(2))

