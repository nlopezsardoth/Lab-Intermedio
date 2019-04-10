import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats
from scipy.optimize import curve_fit


dataact1=np.loadtxt("perfil_7_600s.dat")

x=dataact1[:,0]
y=dataact1[:,1]


plt.scatter(x,y)


plt.plot(x,y)
plt.show()


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


#plt.plot(Oxi1p,Oxi1l,'b+:',label='data')
#plt.plot(Oxi1p,fitoxi1,'ro:',label='fit')
#plt.show()



#ubicacion de las lineas
#Oxi1p=np.array([577,578,579,580,581,582,583])
#Oxi1l=np.array([29087,28362,28157,28226,29044,29996,30712])


Oxi1p=np.array([551,552,553,554,555,556,557,558])
Oxi1l=np.array([29428,28978,28471,28768,29296,30127,30809,31415])

Oxi2p=np.array([559,560,561,562,563,564])
Oxi2l=np.array([29090,28580,28251,28684,29260,30126])

Oxi3p=np.array([683,684,685,686,687,688,689,690,691])
Oxi3l=np.array([28589,28022,27740,26964,27039,27464,28293,28548,29153])

Oxi4p=np.array([775,776,777,778,779,780,781,782])
Oxi4l=np.array([28874,28236,28180,28093,28397,28977,29450,29721])

Oxi5p=np.array([900,901,902,903,904,905])
Oxi5l=np.array([29230,28833,28813,28707,29238,29481])

Oxi6p=np.array([925,926,927,928,929,930,931,932])
Oxi6l=np.array([29446,29141,28785,28613,28894,29555,30227,30571])

Oxi7p=np.array([1035,1036,1037,1038,1039,1040,1041,1042])
Oxi7l=np.array([29101,28769,28478,28387,28820,29196,29732,29938])

Oxi8p=np.array([1088,1089,1090,1091,1092,1093])
Oxi8l=np.array([29155,28876,28445,28761,29111,29486])


Oxip=np.array([Oxi1p,Oxi2p,Oxi3p,Oxi4p,Oxi5p,Oxi6p,Oxi7p,Oxi8p])
Oxil=np.array([Oxi1l,Oxi2l,Oxi3l,Oxi4l,Oxi5l,Oxi6l,Oxi7l,Oxi8l])


def cens(x,y):
	lenp=len(y)
	lenl=len(x)
	pos=[]
	for i in range(lenp):
		pos.append(center(x[i],y[i]))
	return pos


posOxi=cens(Oxip,Oxil)
teoOxi=np.array([6295.96,6298.457,6299.228,6302,6305.81,6306.565,6309.886,6310.636])

m, b, r_value, p_value, err = stats.linregress(posOxi,teoOxi)

def cali(x,y):
	cal=[]
	arr= np.polyfit(x,y,2)
	a=arr[0]
	b=arr[1]
	c=arr[2]
	
	for i in range(len(x)):
		cal.append(a*x[i]**2+b*x[i]+c)
	return cal



#lineas de hierro

hierro1=np.genfromtxt("Minimos_Hierro/Minimo_Hierro1")
hierro2=np.genfromtxt("Minimos_Hierro/Minimo_Hierro2")
hierro3=np.genfromtxt("Minimos_Hierro/Minimo_Hierro3")
hierro4=np.genfromtxt("Minimos_Hierro/Minimo_Hierro4")
hierro5=np.genfromtxt("Minimos_Hierro/Minimo_Hierro5")
hierro6=np.genfromtxt("Minimos_Hierro/Minimo_Hierro6")
hierro7=np.genfromtxt("Minimos_Hierro/Minimo_Hierro7")
#hierro8=np.genfromtxt("Minimos_Hierro/Minimo_Hierro8")









