import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats
from scipy.optimize import curve_fit


dataact1=np.loadtxt("perfil_7_600s.dat")

x=dataact1[:,0]
y=dataact1[:,1]

plt.scatter(x,y)
plt.show()


p = np.array([761, 778, 795, 903, 928, 1038, 1090])
l = np.array([1/6301.508, 1/6302, 1/6302.499, 1/6305.81, 1/6306.565, 1/6309.886, 1/6311.504])


m, b, r_value, p_value, err = stats.linregress(p,l)

def cali(x):
	return 1/(m*x + b)

print (m)
print (b)
