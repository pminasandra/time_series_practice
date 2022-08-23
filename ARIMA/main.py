# Pranav Minasanda & Vivek H Sridhar
# pminasandra.github.io & vivekhsridhar.com
# Aug 23, 2022

import random

from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import linregress

import differencing
import signal_creation

def arima(series, n_pred):
    """
    Generates toy-model ARIMA based predictions for the given time-series.
    Args:
        series (array-like): series upon which to do forecasting
        n_pred (int): number of points used in prediction in every iteration
    """

    assert len(series) > n_pred, "series is smaller than n_pred."
    predictions = [[], []]

    differenced_series, num_diff = differencing.difference(series) # Differencing
    for i in range(len(differenced_series) - n_pred):
        training_points = differenced_series[i : i+n_pred] #Subset of differences series
        LM = linregress(x=np.arange(i, i+n_pred), y=training_points) # Regression
        predictions[0].append(i+n_pred+1)
        training_points = list(training_points)
        training_points.append(LM.slope*(i+n_pred+1) + LM.intercept)

        training_points = differencing.dedifference(np.array(training_points), num_diff) # Dedifferencing
        predictions[1].append(training_points[-1])

    return np.array(predictions)

def main():

    x1 = signal_creation.generate_signal(0, 500, 1, [0.1, 1], 0.1)
        return a*np.sin(0.02513272*0.5*x) + b*np.cos(0.02513272*0.7*x + c) + c*np.sin(0.02513272*0.3*x + b)
    x2 = signal_creation.generate_signal2(0, 5000, 1, _sin_with_freq, 1)
    x3 = signal_creation.generate_signal(0, 500, 1, [-1, 1, 1], 1)

    x1_preds = arima(x1[1], 5)
    print(x1[1].shape)

    x2_preds = arima(x2[1], 5)
    
#    x3_preds = arima(x3[1], 25)

    fig, axs = plt.subplots(3,1)
    axs[0].scatter(x1[0], x1[1])
    axs[0].scatter(x1_preds[0], x1_preds[1], color="red", label="toy-ARIMA predictions", s=0.1)
    axs[0].legend()

    axs[1].scatter(x2[0], x2[1])
    axs[1].scatter(x2_preds[0], x2_preds[1], color="red", label="prediction", s=0.1)
    axs[1].legend()

#    axs[0].scatter(x1[0], x1[1])
#    axs[0].plot(x1_preds[0], x1_preds[1], color="red", label="prediction")
#    axs[0].legend()


    plt.show()

if __name__ == "__main__":
    main()
