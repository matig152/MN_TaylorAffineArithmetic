from affine_form import AffineForm
import numpy as np
import math # FOR BINOMIAL COEFF


# MATRIX B 
def build_B_matrix(n, x0, x1):
    B = np.zeros((n,n))
    for i in range(n):
        for j in range(i,n):
            B[i, j] = math.comb(j, i) * (x0**(j-i)) * (x1**i)
    return B

# MATRIX C
def build_C_matrix(m,n,y0, y1):
    C = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if i >= j:
                C[i, j] = math.comb(i,j) * (y0**(i-j)) * (y1 ** j)
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
    C = build_C_matrix(A.shape[1], A.shape[0], y.center, y.noise_terms[0])
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

    return (f_lower, f_upper)



def compute_bounds_two_var(x, y, A):
    B = build_B_matrix(A.shape[0], x.center, x.noise_terms[0])
    C = build_C_matrix(A.shape[1], A.shape[0], y.center, y.noise_terms[0])
    V = np.matmul(B, A)
    V = np.matmul(V, C)
    n, m = V.shape
    f_upper = V[0, 0]
    f_lower = V[0, 0]

    # TERM 1 - i varies
    for i in range(1,n):
        if i % 2 == 0:
            f_upper += max(0, V[i, 0])
            f_lower += min(0, V[i, 0])     
        else:
            f_upper += abs(V[i, 0])
            f_lower += (-1) * abs(V[i, 0])
    
    # TERM 2 - j varies
    for j in range(1,m):
        if j % 2 == 0:
            f_upper += max(0, V[0, j])
            f_lower += min(0, V[0, j])
        else:
            f_upper += abs(V[0, j])
            f_lower += (-1) * abs(V[0, j])
    
    # TERM 3 - i, j varies
    for i in range(1,n):
        for j in range(1,m):
            if i % 2 == 0 and j % 2 == 0:
                f_upper += max(0, V[i, j])
                f_lower += min(0, V[i, j])
            else:
                f_upper += abs(V[i ,j])
                f_lower += (-1)*abs(V[i ,j])

    return (f_lower, f_upper)


def compute_bounds_one_var(y, A):
    B = np.zeros((A.shape[0], A.shape[0]))
    for j in range(B.shape[1]):
        B[0, j] = 1
    C = build_C_matrix(A.shape[0],A.shape[0], y.center, y.noise_terms[0])
    W = np.matmul(B, A)
    W = np.matmul(W, C)

    m = W.shape[0]
    f_upper = W[0]
    f_lower = W[0]
    # TERM 1 - j varies
    for j in range(1,m):
        if j % 2 == 0:
            f_upper += max(0, W[j])
            f_lower += max(0, W[j])
        else:
            f_upper += abs(W[j])
            f_lower -= abs(W[j])

    return (f_lower, f_upper)


def compute_bounds(var_list, coeff_tensor):
    n_variables = len(var_list)
    if n_variables != coeff_tensor.ndim:
        print("Number of variables does not match tensor dimension.")
        return
    
    if n_variables == 3:
        f_lower, f_upper = compute_bounds_three_var(var_list[0], var_list[1], var_list[2], coeff_tensor)
    if n_variables == 2:
        f_lower, f_upper = compute_bounds_two_var(var_list[0], var_list[1], coeff_tensor)
    if n_variables == 1:
        f_lower, f_upper = compute_bounds_one_var(var_list[0], coeff_tensor)
    if n_variables > 3 or n_variables == 0:
        print("Not supported number of variables.")
    return(f_lower, f_upper)

if __name__ == "__main__":

    # EXAMPLE AFFINE FORMS
    x = AffineForm(2, [0.1])
    y = AffineForm(1, [0.2])
    z = AffineForm(3, [0.05])
    # EXAMPLE COEFF TENSOR (A)
    
    A = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

    f_lower, f_upper = compute_bounds([x, y, z], A)
    print(f'Function in [{f_lower}, {f_upper}]')