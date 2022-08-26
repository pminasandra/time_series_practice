# Pranav Minasandra
# pminasandra.github.io
# Aug 26, 2022

import numpy as np
import pandas as pd
from scipy.integrate import odeint

def ode_simulate(function, init, time=np.arange(0,100,0.1), noise=0.5):
    """
    Simulates a given ODE for a given time-span.
    Args:
        function (callable): returns derivative of state vector
        init (list like): starting conditions for dynamical equation
        time (numpy array): times at which to report dynamical equation results
        noise (float): variance for gaussian measurement noise
    Returns:
        pd.DatFrame() object containing all data
    """

    vec_init = init
    res = odeint(function, vec_init, time)
    res += noise*np.random.randn(res.shape[0], res.shape[1])
    return res.T

def lorenz_attractor(sigma=10.0, rho=28.0, beta=8.0/3.0):


    def ode(vector, t):
        x, y, z = vector[0], vector[1], vector[2]
        del t
        return sigma*(y - x), x*(rho - z) - y, x*y - beta*z

    return ode

def lotka_volterra(alpha=0.0785, beta=0.157, gamma=0.119, delta=0.119):

    def x_der(vector):
        return alpha*vector[0] - beta*vector[0]*vector[1]

    def y_der(vector):
        return delta*vector[0]*vector[1] - gamma*vector[1]

    def ode(vector, t):
        del t
        return [x_der(vector), y_der(vector)]

    return ode
