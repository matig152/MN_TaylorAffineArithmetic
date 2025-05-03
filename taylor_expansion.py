import sympy as sp
import numpy as np
from itertools import product
from collections import defaultdict

def taylor_expansion(f, variables, exp_point, order):
    """
    Compute Taylor expansion and return both the expansion and coefficients.
    
    Args:
        f: SymPy expression to expand
        variables: List of variables (e.g., [x, y])
        exp_point: Expansion point (e.g., [0, 0])
        order: Maximum order of expansion
        
    Returns:
        tuple: (expanded_expr, coeff_matrix)
        where coeff_matrix[i,j] = coefficient for var1^i * var2^j
    """
    n_vars = len(variables)
    if n_vars != 2:
        raise ValueError("Currently only supports 2 variables")
    
    # Compute Taylor expansion
    expansion = f
    for n in range(1, order):
        # Generate all multi-indices of order n
        exponents = product(range(n+1), repeat=n_vars)
        exponents = [e for e in exponents if sum(e) == n]
        
        for alpha in exponents:
            # Compute partial derivative
            deriv = f
            for var, power in zip(variables, alpha):
                if power > 0:
                    deriv = sp.diff(deriv, var, power)
            
            # Evaluate at expansion point
            deriv_at_point = deriv.subs(dict(zip(variables, exp_point)))
            
            # Polynomial term
            poly_term = 1
            for var, point, power in zip(variables, exp_point, alpha):
                if power > 0:
                    poly_term *= (var - point)**power
            
            # Add term to expansion
            expansion += (sp.factorial(n) / np.prod([sp.factorial(a) for a in alpha])) * \
                        deriv_at_point * poly_term / sp.factorial(n)
    
    # Fully expand the expression
    expanded_expr = sp.expand(expansion)
    
    # Extract coefficients into a dictionary
    coeff_dict = defaultdict(float)
    for term in expanded_expr.as_ordered_terms():
        # Get powers and coefficient for each term
        coeff, powers = term.as_coeff_mul(*variables)
        if not powers:
            coeff_dict[(0, 0)] += float(coeff)
            continue
            
        # Determine powers for each variable
        power_dict = {var: 0 for var in variables}
        for power in powers:
            base, exp = power.as_base_exp()
            if base in variables:
                power_dict[base] = exp if exp.is_Integer else 1
        
        # Store coefficient
        key = tuple(power_dict[var] for var in variables)
        coeff_dict[key] += float(coeff)
    
    # Create coefficient matrix
    max_pows = [max(k[i] for k in coeff_dict.keys()) for i in range(n_vars)]
    coeff_matrix = np.zeros((max_pows[0]+1, max_pows[1]+1))
    
    for (i, j), coeff in coeff_dict.items():
        coeff_matrix[i, j] = coeff
    
    return expanded_expr, coeff_matrix

if __name__ == "__main__":
    # Define variables and function
    mu, s = sp.symbols('mu s')
    f = sp.sqrt(mu * s)

    # Compute 2nd order Taylor expansion around (0, 0)
    taylor, matrix = taylor_expansion(f, [mu, s], [0.7, 0.9], 4)
    
    print(taylor)
    print(matrix)