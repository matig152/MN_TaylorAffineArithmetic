## Taylor Affine Arithmetic
This repository is a Python implementation of the article: [A Taylor-Affine Arithmetic for analyzing the calculation result uncertainty in accident reconstruction,
Forensic Science International](https://www.sciencedirect.com/science/article/abs/pii/S0379073816303152).

## Contents
- `interval.py` - basic interval arithmetic, as described in Appendix A
- `affine_form.py` - affine numbers arithmetic, as described in Appendix B
- `compute_bounds.py` - implements a function for computing polynomial function bounds based on provided affine forms and a coefficient matrix (or tensor), as described in Appendix C. Available for three, two and one independent variable problem.
- `case1.py` - implementation of first numerical case from the article (velocity interval based on $ \mu $ and $ s $)
