from _sum_rain import *
import numpy as np

rain = np.load('rain.npy')
print("Swig", sum_rain(rain))
rain = .1 * rain
rain[rain < 0] = .025
print("Numpy", rain.sum())
