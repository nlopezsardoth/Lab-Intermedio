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


#plt.plot(O1p,O1l,'b+:',label='data')
#plt.plot(O1p,fito1,'ro:',label='fit')
#plt.show()



#ubicacion de las lineas
#O1p=np.array([577,578,579,580,581,582,583])
#O1l=np.array([29087,28362,28157,28226,29044,29996,30712])


O1p=np.array([551,552,553,554,555,556,557,558])
O1l=np.array([29428,28978,28471,28768,29296,30127,30809,31415])

O2p=np.array([559,560,561,562,563,564])
O2l=np.array([29090,28580,28251,28684,29260,30126])

O3p=np.array([683,684,685,686,687,688,689,690,691])
O3l=np.array([28589,28022,27740,26964,27039,27464,28293,28548,29153])

O4p=np.array([775,776,777,778,779,780,781,782])
O4l=np.array([28874,28236,28180,28093,28397,28977,29450,29721])

O5p=np.array([900,901,902,903,904,905])
O5l=np.array([29230,28833,28813,28707,29238,29481])

O6p=np.array([925,926,927,928,929,930,931,932])
O6l=np.array([29446,29141,28785,28613,28894,29555,30227,30571])

O7p=np.array([1035,1036,1037,1038,1039,1040,1041,1042])
O7l=np.array([29101,28769,28478,28387,28820,29196,29732,29938])

O8p=np.array([1088,1089,1090,1091,1092,1093])
O8l=np.array([29155,28876,28445,28761,29111,29486])


Op=np.array([O1p,O2p,O3p,O4p,O5p,O6p,O7p,O8p])
Ol=np.array([O1l,O2l,O3l,O4l,O5l,O6l,O7l,O8l])


def cens(x,y):
	lenp=len(y)
	lenl=len(x)
	pos=[]
	for i in range(lenp):
		pos.append(center(x[i],y[i]))
	return pos


posO=cens(Op,Ol)
teoO=np.array([6295.96,6298.457,6299.228,6302,6305.81,6306.565,6309.886,6310.636])


def caliO(x,y):
	cal=[]
	arr= np.polyfit(x,y,2)
	a=arr[0]
	b=arr[1]
	c=arr[2]
	
	for i in range(len(x)):
		cal.append(a*x[i]**2+b*x[i]+c)
	return cal


lambO = (caliO(posO,teoO))
#[6296.902301164079, 6297.072148266317, 6299.938354291836, 6302.194455914639, 6305.541123820198, 6306.258626162938, 6309.5002014357515, 6311.134788944247]


#lineas de hierro

Fe1=np.genfromtxt("Minimos_Hierro/Minimo_Hierro1")
Fe2=np.genfromtxt("Minimos_Hierro/Minimo_Hierro2")
Fe3=np.genfromtxt("Minimos_Hierro/Minimo_Hierro3")
Fe4=np.genfromtxt("Minimos_Hierro/Minimo_Hierro4")
Fe5=np.genfromtxt("Minimos_Hierro/Minimo_Hierro5")
Fe6=np.genfromtxt("Minimos_Hierro/Minimo_Hierro6")
Fe7=np.genfromtxt("Minimos_Hierro/Minimo_Hierro7")
Fe8=np.genfromtxt("Minimos_Hierro/Minimo_Hierro8")
Fe9=np.genfromtxt("Minimos_Hierro/Minimo_Hierro9")
Fe10=np.genfromtxt("Minimos_Hierro/Minimo_Hierro10")

Fep=np.array([Fe1[:,0],Fe2[:,0],Fe3[:,0],Fe4[:,0],Fe5[:,0],Fe6[:,0],Fe7[:,0],Fe8[:,0],Fe9[:,0],Fe10[:,0]])
Fel=np.array([Fe1[:,1],Fe2[:,1],Fe3[:,1],Fe4[:,1],Fe5[:,1],Fe6[:,1],Fe7[:,1],Fe8[:,1],Fe9[:,1],Fe10[:,1]])

posFe=cens(Fep,Fel)

def caliFe(x,y,z):
	cal=[]
	arr= np.polyfit(x,y,2)
	a=arr[0]
	b=arr[1]
	c=arr[2]
	
	for i in range(len(z)):
		cal.append(a*z[i]**2+b*z[i]+c)
	return cal

lambFe=caliFe(posO,teoO,posFe)
#print (lambFe)


c = 3*10**(8)

teoFe = np.array([6290.974,6297.799,6301.508,6302.499,6311.504,6314.668,6315.314,6315.814,6318.027,6318.61])
l = 1/teoFe


def doppler(x,y):
	a = []
	for i in range(len(x)):
		a.append((c*(x[i]*10**(-10) - y[i]*10**(-10))/y[i]*10**(-10))*np.sin(0.17))
	return a

v = doppler(posFe,l)
print (v)









