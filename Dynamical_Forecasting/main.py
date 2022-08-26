# Pranav Minasandra
# pminasandra.github.io
# Aug 26, 2022

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd

import dynamics
import embedding

time = np.arange(0.0, 40.0, 0.01)

fig, axs = plt.subplots(3,1)
results = dynamics.ode_simulate(dynamics.lorenz_attractor(), [1,1,1], time, noise=10)

predictions = []

for i in range(2000, len(time)):
    pred = embedding.predict(results[:,:i], 2, 5)
    predictions.append(pred)

predictions = np.array(predictions).T

axs[0].plot(results[0,:])
axs[0].plot(range(2000,len(time)), predictions[0,:])
axs[1].plot(results[1,:])
axs[1].plot(range(2000,len(time)), predictions[1,:])
axs[2].plot(results[2,:])
axs[2].plot(range(2000,len(time)), predictions[2,:])

plt.show()

