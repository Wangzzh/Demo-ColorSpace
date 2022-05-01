import numpy as np
from matplotlib import pyplot as plt
from functions import *

wavelengths = np.linspace(400, 700, 61)
L = LColorMatchingFunction()
M = MColorMatchingFunction()
S = SColorMatchingFunction()

plt.plot(wavelengths, L.eval(wavelengths), 'r')
plt.plot(wavelengths, M.eval(wavelengths), 'g')
plt.plot(wavelengths, S.eval(wavelengths), 'b')
plt.legend(["$l(\lambda)$", "$m(\lambda)$", "$s(\lambda)$"])
plt.title("Approximated lms color matching functions")
plt.xlabel("wavelength (nm)")
plt.show()

