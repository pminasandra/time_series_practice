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
half_time = int(np.max(time)/(2*(time[1]-time[0])))

fig, axs = plt.subplots(3,1)
results = dynamics.ode_simulate(dynamics.lorenz_attractor(), [1,1,1], time, noise=5)

predictions = []

for i in range(half_time, len(time)):
    pred = embedding.predict(results[:,:i], 3, 5)
    predictions.append(pred)

predictions = np.array(predictions).T

axs[0].plot(range(half_time,len(time)),results[0,half_time:])
axs[0].plot(range(half_time,len(time)), predictions[0,:])
axs[1].plot(range(half_time,len(time)),results[1,half_time:])
axs[1].plot(range(half_time,len(time)), predictions[1,:])
axs[2].plot(range(half_time,len(time)),results[2,half_time:])
axs[2].plot(range(half_time,len(time)), predictions[2,:])
plt.show()

fig = plt.figure()
ax = fig.gca(projection="3d")
ax.plot(results[0, half_time:], results[1, half_time:], results[2, half_time:])
ax.plot(predictions[0, :], predictions[1, :], predictions[2, :])
plt.show()
