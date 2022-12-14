# Pranav Minasandra
# pminasandra.github.io
# Aug 25, 2022

import numpy as np
import pandas as pd

x = [10]
y = [10]
z = [10]
k = [10]

count = 300

for c in range(count):
    if c <= 1:
        x.append(x[-1])
        k.append(k[-1])
    else:
        x.append(2/3*x[c-1] + 1/3*x[c-2] + np.random.normal(0, 0.1))
        k.append(2/3*z[c-1] + 1/3*x[c-1] + np.random.normal(0, 0.1))

    if c == 0:
        y.append(y[-1])
        z.append(z[-1])
    else:
        y.append(x[c-1] + np.random.normal(0, 0.1))
        z.append(2/3*x[c-1] + 1/3*k[c-1] + np.random.normal(0, 0.1))

dataset = pd.DataFrame(np.array([x, y, z, k]).T[50:,:], columns=['x', 'y', 'z', 'k'])
