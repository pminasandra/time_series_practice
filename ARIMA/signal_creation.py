import numpy as np
import matplotlib.pyplot as plt

def poly_time_series(poly, x, var):
	y = poly(x) + np.random.normal(0,var,len(x))
	return(y)

def generate_signal(tmin, tmax, tstep, coeff, var):
	x = np.arange(tmin, tmax, tstep)
	y = poly_time_series(np.poly1d(coeff), x, var)
	return(x, y)
