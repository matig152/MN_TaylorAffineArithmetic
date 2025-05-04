## Taylor Affine Arithmetic
This repository is a Python implementation of the article: [A Taylor-Affine Arithmetic for analyzing the calculation result uncertainty in accident reconstruction,
Forensic Science International](https://www.sciencedirect.com/science/article/abs/pii/S0379073816303152).

## Contents
- `interval.py` - basic interval arithmetic, as described in Appendix A
- `affine_form.py` - affine numbers arithmetic, as described in Appendix B
- `compute_bounds.py` - implements a function for computing polynomial function bounds based on provided affine forms and a coefficient matrix (or tensor), as described in Appendix C. Available for three, two and one independent variable problem.
- `taylor_expansion.py` - implements taylor expansion for a two variable function. 
- `case1.py` - implementation of first numerical case from the article (velocity interval based on $` \mu `$ and $` s `$)
- `case2.py` - approximation of function $` f(x, y) = \frac{-x^2 + 30x}{-y^2+12y} `$, where $` x \in [10, 20], y \in [4, 8] `$
- `case3.py` - approximation of function $` f(x, y) = x^2 + y `$, where $` x \in [-2, 2], y \in [1, 3] `$
- `case4.py` - approximation of function $` f(x,y) = \frac{-x^2 + 3-x + 10}{-x^2 + 6y} `$, where $` x \in [10, 20], y \in [4, 8] `$
