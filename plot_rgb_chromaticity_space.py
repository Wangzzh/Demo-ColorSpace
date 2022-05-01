from matplotlib import pyplot as plt
import numpy as np
from functions import *

wavelengths = np.linspace(400, 700, 121)
X = XColorMatchingFunction().eval(wavelengths)
Y = YColorMatchingFunction().eval(wavelengths)
Z = ZColorMatchingFunction().eval(wavelengths)
x = X / (X + Y + Z)
y = Y / (X + Y + Z)

grid = np.linspace(0, 1, 41)
R, G, B = np.meshgrid(grid, grid, grid)
RGB = np.array([R.flatten(), G.flatten(), B.flatten()])
RGBtoXYZ = np.array([
    [0.49, 0.31, 0.2],
    [0.177, 0.812, 0.011],
    [0, 0.01, 0.99]
])
XYZ = RGBtoXYZ @ RGB + 0.0001
rgbx = XYZ[0] / (XYZ.sum(axis=0))
rgby = XYZ[1] / (XYZ.sum(axis=0))

plt.plot(x, y, '-')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.xlabel("x")
plt.ylabel("y")

for i in range(len(XYZ[0])):
    plt.plot(rgbx[i], rgby[i], 'o', color=(RGB[0][i], RGB[1][i], RGB[2][i]))

plt.title("rgb space in chromaticity diagram")
plt.show()

