from numpy.random import random_integers
from numpy.random import randn
import numpy as np
import timeit
import argparse
import multiprocessing as mp
import matplotlib.pyplot as plt


def simulate(size):
    n = 0
    mean = 0
    M2 = 0

    speed = randn(10000)

    for i in range(1000): 
        n = n + 1
        indices = random_integers(0, len(speed)-1, size=size)
        x = (1 + speed[indices]).prod()
        delta = x - mean
        mean = mean + delta/n
        M2 = M2 + delta*(x - mean)

    return mean

def serial():
    start = timeit.default_timer()

    for i in range(10, 50):
        simulate(i)
    
    end = timeit.default_timer() - start
    print("Serial time", end)

    return end

def parallel(nprocs):
    start = timeit.default_timer()
    p = mp.Pool(nprocs)
    print(nprocs, "Pool creation time", timeit.default_timer() - start)

    p.map(simulate, [i for i in range(10, 50)])
    p.close()
    p.join()

    end = timeit.default_timer() - start
    print(nprocs, "Parallel time", end)
    return end

if __name__ == "__main__":
    ratios = []
    baseline = serial()

    for i in range(1, mp.cpu_count()):
        ratios.append(baseline/parallel(i))

    plt.xlabel('# processes')
    plt.ylabel('Serial/Parallel')
    n = np.arange(1, mp.cpu_count())
    plt.plot(n, ratios)
    plt.grid(True)
    plt.show()
