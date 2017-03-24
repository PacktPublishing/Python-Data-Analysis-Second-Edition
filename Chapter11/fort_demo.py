import fort_sum
import numpy as np

rain = np.load('rain.npy')
fort_sum.sumarray(rain, len(rain))
rain = .1 * rain
rain[rain < 0] = .025
print("Numpy", rain.sum())
