import numpy as np


class Gaussian:

    def __init__(self, mu, sigma_l, sigma_r):
        self.mu, self.sigma_l, self.sigma_r = mu, sigma_l, sigma_r

    def eval(self, val):
        return np.piecewise(val, [val <= self.mu, val > self.mu], [
            lambda x: np.exp(-(x - self.mu) * (x - self.mu) / 2 / self.sigma_l / self.sigma_l),
            lambda x: np.exp(-(x - self.mu) * (x - self.mu) / 2 / self.sigma_r / self.sigma_r)
        ])


class XColorMatchingFunction:

    def __init__(self):
        self.g1 = Gaussian(599.8, 37.9, 31.0)
        self.g2 = Gaussian(442.0, 16.0, 26.7)
        self.g3 = Gaussian(501.1, 20.4, 26.2)

    def eval(self, val):
        return 1.056 * self.g1.eval(val) + 0.362 * self.g2.eval(val) - 0.065 * self.g3.eval(val)


class YColorMatchingFunction:

    def __init__(self):
        self.g1 = Gaussian(568.8, 46.9, 40.5)
        self.g2 = Gaussian(530.9, 16.3, 31.1)

    def eval(self, val):
        return 0.821 * self.g1.eval(val) + 0.286 * self.g2.eval(val)


class ZColorMatchingFunction:

    def __init__(self):
        self.g1 = Gaussian(437.0, 11.8, 36.0)
        self.g2 = Gaussian(459.0, 26.0, 13.8)

    def eval(self, val):
        return 1.217 * self.g1.eval(val) + 0.618 * self.g2.eval(val)


class LColorMatchingFunction:

    def __init__(self):
        self.x = XColorMatchingFunction()
        self.y = YColorMatchingFunction()
        self.z = ZColorMatchingFunction()

    def eval(self, val):
        return 0.38971 * self.x.eval(val) + 0.68898 * self.y.eval(val) - 0.07868 * self.z.eval(val)


class MColorMatchingFunction:

    def __init__(self):
        self.x = XColorMatchingFunction()
        self.y = YColorMatchingFunction()
        self.z = ZColorMatchingFunction()

    def eval(self, val):
        return -0.22981 * self.x.eval(val) + 1.18341 * self.y.eval(val) + 0.04640 * self.z.eval(val)


class SColorMatchingFunction:

    def __init__(self):
        self.z = ZColorMatchingFunction()

    def eval(self, val):
        return self.z.eval(val)


class RColorMatchingFunction:

    def __init__(self):
        self.x = XColorMatchingFunction()
        self.y = YColorMatchingFunction()
        self.z = ZColorMatchingFunction()

    def eval(self, val):
        return 2.36461 * self.x.eval(val) - 0.89654 * self.y.eval(val) - 0.46807 * self.z.eval(val)


class GColorMatchingFunction:

    def __init__(self):
        self.x = XColorMatchingFunction()
        self.y = YColorMatchingFunction()
        self.z = ZColorMatchingFunction()

    def eval(self, val):
        return -0.51517 * self.x.eval(val) + 1.42640 * self.y.eval(val) + 0.08875 * self.z.eval(val)


class BColorMatchingFunction:

    def __init__(self):
        self.x = XColorMatchingFunction()
        self.y = YColorMatchingFunction()
        self.z = ZColorMatchingFunction()

    def eval(self, val):
        return 0.00520 * self.x.eval(val) - 0.01441 * self.y.eval(val) + 1.00920 * self.z.eval(val)