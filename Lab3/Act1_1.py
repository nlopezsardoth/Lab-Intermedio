import numpy as np
import matplotlib.pyplot as plt
#import statistics as stats
import math
from scipy.optimize import curve_fit

dataact1=np.loadtxt("Datos_1.txt", skiprows=1)

dmin=dataact1[:,0]
lamb=dataact1[:,1]

def rad(grad):
	rad=grad*(np.pi /180.0)
	return rad

alfa=rad(60)
n=[]

for i in range(len(dmin)):
	n.append((np.sin((alfa+rad(dmin[i]))/2.0))/(np.sin(alfa/2.0)))

ll=[]

for i in range(len(lamb)):
	ll.append(1/((lamb[i])**2))

print (n)

#plt.figure(1)
#plt.plot(ll,n)
#plt.ylabel('n')
#plt.xlabel('lambda^2')
#plt.title('n vs lambda')

#plt.figure(2)
#plt.plot(lamb,n)
#plt.ylabel('n')
#plt.xlabel('lambda')
#plt.title('n vs lambda')
#plt.show()


def func(A, B, lamb):
	return A + B/(lamb**2)

popt, pcov = curve_fit(func, lamb, n)

plt.plot(lamb, func(lamb, *popt))
#plt.plot(lamb,n)
plt.show()




