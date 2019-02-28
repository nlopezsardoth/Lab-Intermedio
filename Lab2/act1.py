import numpy as np
import matplotlib.pyplot as plt
import statistics as stats
import math

#####Parte 1######

dataact1=np.loadtxt("Data1-1.txt", skiprows=1)

d=dataact1[:,0]
c=dataact1[:,1]

mean= stats.mean(c)

#print (mean)

deviation= stats.stdev(c)

#print (deviation)

dataact1_2=np.loadtxt("Data1-2.txt", skiprows=1)
t=dataact1_2[:,1]
c=dataact1_2[:,2]
c1= c[3:]
mean= stats.mean(c1)
#print (mean)

######Parte 2#####
data_3=np.loadtxt("Data1-3.txt", skiprows=1)

n=data_3[:,0]
c=data_3[:,1]

d=[]
for i in range(len(c)):
	d.append(c[i]-5)
d[0]=79

mean=stats.mean(d)
ss= stats.stdev(d)
print (ss)
sigma=math.sqrt(mean)

print ("mean = ", mean)

print ("sigma = ", sigma)

error_mean= stats.stdev(d)/(math.sqrt(len(d)))
print ("error mean = ", error_mean)

error_sigma=(1.0/(2.0*math.sqrt(mean)))*(error_mean)
print ("error sigma = ", error_sigma)

plt.hist(d, color = 'grey', edgecolor = 'black')
plt.ylabel('Frecuencia')
plt.xlabel('C')
#plt.savefig("Lab2_fig1.png")
