import numpy as np
from scipy import stats
from scipy.optimize import curve_fit

p = np.array([760, 776, 793, 902, 926, 1036, 1090])
l = np.array([1/6301.508, 1/6302, 1/6302.499, 1/6305.81, 1/6306.565, 1/6309.886, 1/6311.504])

m, b, r_value, p_value, err = stats.linregress(p,l)

def cali(x):
	return 1/(m*x + b)

print (m)
print (b)

pu=761

la=m*pu+b
print (1/la)
