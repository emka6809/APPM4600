# import libraries 
import numpy as np
import scipy
from scipy import special
import matplotlib.pyplot as plt

x = np.linspace(0,2)
denom = 2 * np.sqrt(0.138 * 10**-6 * 60 * 86400)
y = special.erf(x / denom) - 3/7

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
