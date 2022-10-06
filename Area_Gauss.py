# Fórmula del área de Gauss para poligonos simples

# %% Librerías
#import math
#import numpy as np

# %% Puntos de un cuadrado en el primer cuadrante
#p = np.array([[0,0],[0,1],[1,1],[1,0]])

#x= p[:,0]
#y= p[:,1]
#del t,p

# %% Puntos de una elipse centrada en (h,k)
# h = 0.0; k = 0.0 #Coordenadas del centro
# a = 1.0; b = 1.0 #Radio mayor, radio menor
# t =np.linspace(0,2.0*math.pi,90000)
# p = np.transpose(np.array([(a*np.cos(t))+h,(b*np.sin(t))+k]))
# a = a*b*math.pi #Area de la elipce

#x= p[:,0]
#y= p[:,1]
#del t,p

# %% Lectura de archivos

# Puntos de X
datos=open('PuntosX.txt','r')
x = datos.read().split('\n')
datos.close()   
x = list(map(float,x))

# Puntos de Y
datos=open('PuntosY.txt','r')
y = datos.read().split('\n')
datos.close()
y = list(map(float,y))

# Dellocate
del datos

# %% Algoritmo
#x= p[:,0]
#y= p[:,1]

A = 0.0

for i in range(len(x)-1):
       A=A+x[i]*y[i+1]-x[i+1]*y[i]
    
A = 0.5*abs(A+x[-1]*y[0]-x[0]*y[-1])

print(str(A))

#E = abs((a-A)/a)