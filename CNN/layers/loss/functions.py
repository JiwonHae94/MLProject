import numpy as np

def softmax(x):
    return x

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)

"""

"""
def cross_entropy_error(y, t):
    delta = 1e-6
    return -1 * np.sum(t * np.log(y + delta))