# Pranav Minasandra
# pminasandra.github.io
# Aug 25, 2022

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.integrate import odeint
from statsmodels.tsa.stattools import grangercausalitytests as gct

from dynamics import dataset

var_names = list(dataset.columns)
scores = np.zeros((len(var_names),len(var_names)))
scores2 = np.zeros((len(var_names),len(var_names)))

for i in range(len(var_names)):
    for j in range(len(var_names)):
        gct_res = gct(dataset[[var_names[i], var_names[j]]], 4)
        if gct_res[1][0]['ssr_ftest'][1] < 0.01:
            scores[i, j] += 1
        if gct_res[2][0]['ssr_ftest'][1] < 0.01:
            scores2[i, j] += 1

print("First day results:")
print(scores)
print("Second day results:")
print(scores2)
for name in var_names:
    plt.plot(dataset[name])

plt.show()
