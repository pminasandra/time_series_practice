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
    res = odeint(function, init, time)
    res += noise*np.random.randn(res.shape[0], res.shape[1])
    return res

def lorenz_attractor(sigma=25, rho=10, beta=4):

    def x_der(vector):
        return sigma*(vector[1] - vector[0])

    def y_der(vector):
        return x*(rho -z) - y

    def z_der(vector):
        return x*y - beta*z

    def ode(vector):
        return (x_der(vector), y_der(vector), z_der(vector))

    return ode

def lotka_volterra(alpha=0.66, beta=1.33, gamma=1, delta=1):

    def x_der(vector):
        return alpha*vector[0] - beta*vector[0]*vector[1]

    def y_der(vector):
        return delta*vector[0]*vector[1] - gamma*vector[1]

    def ode(vector):
        return (x_der(vector), y_der(vector))

    return ode
