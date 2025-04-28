from affine_form import AffineForm
import numpy as np
import math # FOR BINOMIAL COEFF

# EXAMPLE AFFINE FORMS
x = AffineForm(2, [0.1])
y = AffineForm(1, [0.2])
z = AffineForm(3, [0.05])
# EXAMPLE COEFF TENSOR (A)
A = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])


# MATRIX B 
def build_B_matrix(n, x0, x1):
    B = np.zeros((n,n))
    for i in range(n):
        for j in range(i,n):
            B[i, j] = math.comb(j, i) * (x0**(j-i)) * (x1**i)
    return B

# MATRIX C
def build_C_matrix(m, y0, y1):
    C = np.zeros((m,m))
    for i in range(m):
        for j in range(m):
            if i >= j:
                C[i, j] = math.comb(j,i) * (y0**(i-j)) * (y1 ** j)
    return C

# MATRIX D
def build_D_matrix(l, z0, z1):
    D = np.zeros((l, l))
    for i in range(l):
        for j in range(i,l):
            D[i,j] = math.comb(j,i) * (z0 ** (j-i)) * (z1**i)
    return D

# MATRIX G
def build_G_matrix(A, B, C, D):
    DA = np.tensordot(D, A, axes=(1,2))
    BDA = np.tensordot(B, DA, axes=(1,1))
    G = np.tensordot(BDA, C, axes=(2,0))
    return G

# COMPUTE UPPER AND LOWER BOUND
def compute_bounds_three_var(x, y, z, A):
    B = build_B_matrix(A.shape[0], x.center, x.noise_terms[0])
    C = build_C_matrix(A.shape[1], y.center, y.noise_terms[0])
    D = build_D_matrix(A.shape[2], z.center, z.noise_terms[0])
    G = build_G_matrix(A, B, C, D)

    n, l, m = G.shape
    f_upper = G[0, 0, 0]
    f_lower = G[0, 0, 0]

    # TERM 1 - k varies
    for k in range(m):
        coeff = G[0, 0, k]
        if k % 2 == 0:
            f_upper += max(0, coeff)
            f_lower += min(0, coeff)
        else:
            f_upper += abs(coeff)
            f_lower += (-1) * abs(coeff)

    # TERM 2 - j, k vary
    for j in range(l):
        for k in range(m):
            coeff = G[0, j, k]
            if j % 2 == 0 and k % 2 == 0:
                f_upper += max(0, coeff)
                f_lower += min(0, coeff)
            else:
                f_upper += abs(coeff)
                f_lower += (-1) * coeff

    # TERM 3 - i, j, k vary
    for i in range(n):
        for j in range(l):
            for k in range(m):
                coeff = G[i, j, k]
                if i % 2 == 0 and j % 2 == 0 and k % 2 == 0:
                    f_upper += max(0, coeff)
                    f_lower += min(0, coeff)
                else:
                    f_upper += abs(coeff)
                    f_lower += (-1) * abs(coeff)

    print(f'Upper bound: {f_upper}')
    print(f'Lower bound: {f_lower}')

    

if __name__ == "__main__":
    compute_bounds_three_var(x, y, z, A)