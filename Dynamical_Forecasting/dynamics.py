# Pranav Minasandra
# pminasandra.github.io
# Aug 26, 2022

import numpy as np
import pandas as pd
from scipy.integrate import odeint

def simulate(function, init, time=np.arange(0,100,0.1), noise=0.5):
    """
    Simulates a given ODE for a given time-span.
    Args:
        function (callable): 
    """

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
