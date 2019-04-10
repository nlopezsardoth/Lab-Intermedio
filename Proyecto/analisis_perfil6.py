import numpy as np
import matplotlib.pyplot as plt
import math


dataact1=np.loadtxt("perfil_6_600s.dat")

x=dataact1[:,0]
y=dataact1[:,1]

plt.scatter(x,y)
plt.show()
