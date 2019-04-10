import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats
from scipy.optimize import curve_fit


dataact1=np.loadtxt("perfil_7_600s.dat")

x=dataact1[:,0]
y=dataact1[:,1]


#plt.scatter(x,y)


#plt.plot(x,y)
#plt.show()

#ubicacion de las lineas
Oxi1p=np.array([577,578,579,580,581,582,583])
Oxi1l=np.array([29087,28362,28157,28226,29044,29996,30712])


def fit(x,y):
	arr=np.polyfit(x,y,2)
	a=arr[0]
	b=arr[1]
	c=arr[2]
	return a,b,c

def center(x,y):
	a,b,c=fit(x,y)
	fito=a*x**2+b*x+c
	center=-b/(2*a)
	return center

print center(Oxi1p,Oxi1l)



#plt.plot(Oxi1p,Oxi1l,'b+:',label='data')
#plt.plot(Oxi1p,fitoxi1,'ro:',label='fit')
#plt.show()


