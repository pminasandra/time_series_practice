# Pranav Minasandra
# pminasandra.github.io
# Aug 26, 2022

import numpy as np
import scipy.spatial.distance
import pandas as pd

def predict(time_series, embed_dimensions=2, num_nearest_neighbours=5):
    """
    predicts next value for time-series based on history
    Args:
        time-series (array like)
        embed_dimensions (int)
        num_nearest_neighbours (int)

    Returns:
        float
    """

    predictions = []
    time_series = time_series.T
    for embed_point in range(embed_dimensions):
        point_val = time_series[-(embed_point+1), :]
        time_series2 = list(time_series)
        distances = np.array([scipy.spatial.distance.euclidean(point, point_val) for point in time_series2])[:-embed_dimensions]

        distances = distances.argsort()[:num_nearest_neighbours]

        for predicting_point in distances:
            predictions.append(time_series[predicting_point + embed_point + 1])

    return np.array(predictions).mean(axis=0)
