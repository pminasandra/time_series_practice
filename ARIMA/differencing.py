# Pranav Minasandra
# pminasandra.github.io
# Aug 23, 2022

from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import linregress

def difference(series, max_iter=10, slope_threshold=0.05):
    """
    Progressively differences the array until the slope is close to 0.
    Args:
        series (array-like): time-series data
        max_iter (int): maximum number of differencing steps allowed
        slope_threshold (float): absolute value of slope threshold at which differencing is to be stopped

    Returns:
        (array-like, int): tuple with differences series and number of differences
    """

    LM = linregress(x=np.arange(0, len(series)), y=series)
    num_diff = 0
    while abs(LM.slope) > slope_threshold:
        series = np.diff(series)
        LM = linregress(x=np.arange(0, len(series)), y=series)
        num_diff += 1
        if num_diff > max_iter and abs(LM.slope) > slope_threshold:
            raise ValueError("max_iter reached but differencing not successful.")

    return series, num_diff

def dedifference(series, num_diff):
    """
    Dedifferences the series n times.
    Args:
        series (array-like): differenced time-series.
        num_diff (int): number of times to dedifference.
    """
    for i in range(num_diff):
        series = series.cumsum()

    return series
