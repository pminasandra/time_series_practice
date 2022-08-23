# Pranav Minasanda & Vivek H Sridhar
# pminasandra.github.io & vivekhsridhar.com
# Aug 23, 2022

import random

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress

import differencing
import signal_creation

SCATTER_SIZE = 10

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
    x2 = signal_creation.combination_of_waves(np.arange(0,4000), 4, np.array([1,1,7,0.4]), np.array([500, 200, 1000, 40]), np.array([-0.78, 0.1, 0.3, 1.57]))
    x3 = pd.read_csv('jena_climate_2009_2016.csv', sep=',', header=0)['T (degC)'].to_numpy()[:10000]

    x1_preds = arima(x1[1], 10)
    x2_preds = arima(x2[1], 10)
    x3_preds = arima(x3, 10)

    fig, axs = plt.subplots(3,1, layout='tight')
    axs[0].scatter(x1[0], x1[1], s=SCATTER_SIZE, label="Real data")
    axs[0].plot(x1_preds[0], x1_preds[1], color="red", label="toy-ARIMA predictions")
    axs[0].legend()
    axs[0].set_title('Linear growth with noise')

    axs[1].scatter(x2[0], x2[1], s=SCATTER_SIZE)
    axs[1].plot(x2_preds[0], x2_preds[1], color="red")
    axs[1].set_title('Combination of random sine waves')

    axs[2].scatter(np.arange(0, len(x3)), x3, s=SCATTER_SIZE)
    axs[2].plot(x3_preds[0], x3_preds[1], color="red")
    axs[2].set_title('Jena Climate Data: Temperature in deg C')


    plt.show()

if __name__ == "__main__":
    main()
