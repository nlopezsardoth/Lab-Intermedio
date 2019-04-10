import numpy as np
import matplotlib.pyplot as plt
import math


datasol=np.loadtxt("catalogo_sol.dat")
dataatm=np.loadtxt("catalogo_atm.dat")

xs=datasol[:,0]
ys=datasol[:,1]

xa=dataatm[:,0]
ya=dataatm[:,1]


plt.stem(xs,      ys, 'b', markerfmt='bo', label='sin')
plt.stem(xa, ya, 'g', markerfmt='go', label='cos')

plt.show()
