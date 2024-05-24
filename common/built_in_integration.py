import numpy as np
import scipy as sc

def alpha(f):
    p = np.pi

    integrand = lambda t: np.square(np.sin(2*p*f*t) + 0.1 * np.sin(6*p*f*t))

    integral = sc.integrate.quad(integrand, 0, 1/f)

    result = np.power(f*integral[0], -0.5)

    return result

print(alpha(50))
print(alpha(1))