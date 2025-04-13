class Interval:
    def __init__(self, inf, sup):
        if inf > sup:
            raise ValueError("Infimum greater than supremum.")
        self.inf = inf
        self.sup = sup

    def __contains__(self, x):
        return self.inf <= x <= self.sup
    
    # TO STRING
    def __str__(self):
        return f'[{self.inf}, {self.sup}]'
    
    # STANDARIZATION
    def standardize(self):
        denom = max(abs(self.inf), abs(self.sup))
        return Interval(self.inf / denom, self.sup / denom)
    
    # ARITHMERIC OPERATIONS
    def __add__(self, other):
        return Interval(self.inf + other.inf, self.sup + other.sup)
    def __sub__(self, other):
        return Interval(self.inf - other.inf, self.sup - other.sup)
    def __mul__(self, other):
        S = [self.inf * other.inf, self.inf * other.sup, self.sup * other.inf, self.sup * other.sup]
        return Interval(min(S), max(S))
    def __truediv__(self, other):
        if (other.contains(0)):
            raise ValueError("Interval contains zero. Cannot be inversed.")
        y_inv = Interval(1 / other.sup(), 1 / other.inf())
        return self * y_inv
    def scalar_mul(self, scalar):
        if(scalar > 0):
            return Interval(self.inf * scalar, self.sup * scalar)
        if(scalar <= 0):
            return Interval(self.sup * scalar, self.inf * scalar)
    

