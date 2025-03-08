import numpy as np

def gaussian(x, mean, var):
    return np.exp(-(x-mean)**2 / (2*var))
