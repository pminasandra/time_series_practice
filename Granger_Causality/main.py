# Pranav Minasandra
# pminasandra.github.io
# Aug 25, 2022

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyinform
from scipy.integrate import odeint
from statsmodels.tsa.stattools import grangercausalitytests as gct

from dynamics import dataset

var_names = list(dataset.columns)
scores = np.zeros((len(var_names),len(var_names)))
scores2 = np.zeros((len(var_names),len(var_names)))
transfer_entropies = np.zeros((len(var_names),len(var_names)))
for name in var_names:
    plt.plot(dataset[name])

plt.xlabel("Time")
plt.ylabel("Values of dynamical variables")
plt.savefig('figures/equations.png')

for i in range(len(var_names)):
    for j in range(len(var_names)):
        gct_res = gct(dataset[[var_names[i], var_names[j]]], 4)
        if gct_res[1][0]['ssr_ftest'][1] < 0.01:
            scores[i, j] += 1
        if gct_res[2][0]['ssr_ftest'][1] < 0.01:
            scores2[i, j] += 1
        transfer_entropies[i,j] += pyinform.transfer_entropy(dataset[var_names[i]], dataset[var_names[j]], k=2)

print("First day results:")
print(scores)
print("Second day results:")
print(scores2)

print("Transfer entropies:")
print(pd.DataFrame(transfer_entropies))
