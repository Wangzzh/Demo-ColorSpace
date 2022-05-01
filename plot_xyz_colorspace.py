import numpy as np
from matplotlib import pyplot as plt
from functions import XColorMatchingFunction, YColorMatchingFunction, ZColorMatchingFunction

wavelengths = np.linspace(400, 700, 61)
X = XColorMatchingFunction()
Y = YColorMatchingFunction()
Z = ZColorMatchingFunction()

plt.plot(wavelengths, X.eval(wavelengths), 'r')
plt.plot(wavelengths, Y.eval(wavelengths), 'g')
plt.plot(wavelengths, Z.eval(wavelengths), 'b')
plt.legend(["$x(\lambda)$", "$y(\lambda)$", "$z(\lambda)$"])
plt.title("Approximated xyz color matching functions")
plt.xlabel("wavelength (nm)")
plt.show()