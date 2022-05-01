from matplotlib import pyplot as plt
import numpy as np
from functions import *

wavelengths = np.linspace(400, 700, 121)
X = XColorMatchingFunction().eval(wavelengths)
Y = YColorMatchingFunction().eval(wavelengths)
Z = ZColorMatchingFunction().eval(wavelengths)
x = X / (X + Y + Z)
y = Y / (X + Y + Z)

sparse_wavelengths = np.array([460, 480, 500, 520, 540, 560, 580, 600, 620], dtype=float)
sX = XColorMatchingFunction().eval(sparse_wavelengths)
sY = YColorMatchingFunction().eval(sparse_wavelengths)
sZ = ZColorMatchingFunction().eval(sparse_wavelengths)
sx = sX / (sX + sY + sZ)
sy = sY / (sX + sY + sZ)

plt.plot(x, y, '-')
plt.plot(sx, sy, 'ko')
plt.xlim([0, 1])
plt.ylim([0, 1])
for i in range(len(sx)):
    plt.annotate(sparse_wavelengths[i], (sx[i] + 0.02, sy[i] + 0.02))
plt.xlabel("x")
plt.ylabel("y")
plt.title("xy chromaticity diagram")
plt.show()

