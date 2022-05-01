import numpy as np
from matplotlib import pyplot as plt
from functions import *

wavelengths = np.linspace(400, 700, 61)
R = RColorMatchingFunction()
G = GColorMatchingFunction()
B = BColorMatchingFunction()

plt.plot(wavelengths, R.eval(wavelengths), 'r')
plt.plot(wavelengths, G.eval(wavelengths), 'g')
plt.plot(wavelengths, B.eval(wavelengths), 'b')
plt.legend(["$r(\lambda)$", "$g(\lambda)$", "$b(\lambda)$"])
plt.title("Approximated rgb color matching functions")
plt.xlabel("wavelength (nm)")
plt.show()