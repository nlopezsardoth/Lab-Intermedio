import numpy as np
import matplotlib.pyplot as plt
import statistics as stats
import math

dataact1=np.loadtxt("Data3-1.txt", skiprows=1)

d=dataact1[:,1]
c=dataact1[:,2]

plt.figure(1)
plt.plot(d,c)
plt.ylabel('Conteos')
plt.xlabel('Distancia [cm]')
plt.title('Conteos vs Distancia [cm]')
#plt.savefig("Lab2_fig2.png")

dd=[]

for i in range(len(d)):
	dd.append(1.0/(d[i]**2))

z = np.polyfit(dd, c,1)
p = np.poly1d(z)

xp = np.linspace(0, 6000, 100)

plt.figure(2)
plt.plot(dd,c)
plt.plot(p(xp),c)

plt.ylabel('Conteos')
plt.xlabel('Distancia [cm]')
plt.title('Conteos vs Distancia [cm]')
plt.show()
