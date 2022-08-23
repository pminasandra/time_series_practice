# Vivek Hari Sridhar
# vivekhsridhar.com
# Aug 23, 2022

import random

import numpy as np
import matplotlib.pyplot as plt

def poly_time_series(poly, x, var):
	y = poly(x) + np.random.normal(0,var,len(x))
	return(y)

def generate_signal2(tmin, tmax, tstep, func, var):
    x = np.arange(tmin, tmax, tstep)
    y = func(x)
    return x,y

def generate_signal(tmin, tmax, tstep, coeff, var):
	x = np.arange(tmin, tmax, tstep)
	y = poly_time_series(np.poly1d(coeff), x, var)
	return(x, y)

def _combination_of_waves(x):
    a, b, c = random.random(), random.random(), random.random()
