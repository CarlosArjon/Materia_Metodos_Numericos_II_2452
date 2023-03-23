import tools.numeric_method.numeric_method as numeric_method
import math
import numpy as np
import sympy as sym


class LagrangePolynomials(numeric_method.NumericMethod):
    def __init__(self, xi, fi, n, x) -> None:

        self.xi = xi
        self.fi = fi
        self.n = n
        self.x = x
        self.polinomio = 0
        self.divisorL = np.zeros(n, dtype=float)

    def logic_numeric_method(self):

        for i in range(0, self.n, 1):

            numerador = 1
            denominador = 1
            for j in range(0, self.n, 1):
                if j != i:
                    numerador = numerador * (self.x - self.xi[j])
                    denominador = denominador * (self.xi[i] - self.xi[j])
            terminoLi = numerador / denominador

            print(terminoLi)

            self.polinomio = self.polinomio + terminoLi * self.fi[i]
            self.divisorL[i] = denominador

        return self.polinomio

    def error_calculation(self):
        pass

    def parameter_validation(self) -> None:
        pass
