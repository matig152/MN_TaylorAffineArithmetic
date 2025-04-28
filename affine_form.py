from interval import Interval

class AffineForm():
    def __init__(self, center, noise_terms=None):
        self.center = center
        self.noise_terms = noise_terms

    def __str__(self):
        string = f'{self.center}'
        for idx, noise_term in enumerate(self.noise_terms):
            string += f' + {noise_term} * eps{idx+1}'
        return string
    
    # CONVERT TO INTERVAL
    def to_interval(self):
        radius = sum(abs(v) for v in self.noise_terms)
        return Interval(self.center - radius, self.center + radius)
    
    # CREATE FROM INTERVAL
    @staticmethod
    def from_interval(interval):
        center = (interval.inf + interval.sup) / 2
        radius = (interval.sup - interval.inf) / 2
        return AffineForm(center, [radius])
    
    # ARITHMETIC OPERATIONS
    def __add__(self, other):
        if len(self.noise_terms) != len(other.noise_terms):
            raise ValueError("Number of noise terms does not match.")
        new_noise_terms = [sum(x) for x in zip(self.noise_terms, other.noise_terms)]
        return AffineForm(self.center + other.center, new_noise_terms)
    
    def __sub__(self, other):
        if len(self.noise_terms) != len(other.noise_terms):
            raise ValueError("Number of noise terms does not match.")
        new_noise_terms = [x - y for x, y in zip(self.noise_terms, other.noise_terms)]
        return AffineForm(self.center - other.center, new_noise_terms)
    
    def scalar_add(self, scalar):
        return AffineForm(scalar + self.center, self.noise_terms)
    
    def scalar_mul(self, scalar):
        new_noise_terms = []
        for i in range(len(self.noise_terms)):
            new_noise_terms.append(self.noise_terms[i] * scalar)
        return AffineForm(scalar * self.center, new_noise_terms)
    

    # MULTIPLICATION USING CHEBYSHEV AFFINE APPROXIMATION (EQ. 8, APPENDIX C)
    def __mul__(self, other):
        if len(self.noise_terms) != len(other.noise_terms):
            raise ValueError("Number of noise terms does not match.")

        # CENTER
        new_center = self.center * other.center
        
        # LINEAR TERMS
        new_noise_terms = []
        for xi, yi in zip(self.noise_terms, other.noise_terms):
            new_noise_terms.append(self.center * xi + other.center * yi)

        # NON-LINEAR TERMS (Q)
        terms = []
        for i in range(len(self.noise_terms)):
            for j in range(len(self.noise_terms)):
                coeff = self.noise_terms[i] * other.noise_terms[j]
                if i == j:
                    # e_i^2 in [0,1], so term in [0, coeff]
                    terms.append((min(0, coeff), max(0, coeff)))
                else:
                    # e_i * e_j in [-1,1], so term in [-|coeff|, |coeff|]
                    terms.append((-abs(coeff), abs(coeff)))


        a = sum(term[0] for term in terms)
        b = sum(term[1] for term in terms)

        new_center += (a + b) / 2
        nonlinear_error = (b - a) / 2
        new_noise_terms.append(nonlinear_error)

        return AffineForm(new_center, new_noise_terms)
