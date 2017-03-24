import numpy as np
import librain

rain_data = np.load('rain.npy')
print("Boost", librain.sum_rain(rain_data.astype(int).tolist(), len(rain_data)))
rain_data = .1 * rain_data
rain_data[rain_data < 0] = .025
print("Numpy", rain_data.sum())
