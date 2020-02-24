import numpy as np
import math
from matplotlib import pyplot
#elegimos sin(x) grado=1

#necesitamo X=X_1,..., x_n, x_n+1,x_n+2
#Con grado 1 solo necesitamos tres puntos
#dichos puntos son los siguintes
puntosIniciales=[-math.pi/64,math.pi/128,math.pi/64]
#construimos el Polinomio
m=np.matrix(
  [[1,puntosIniciales[0],1],
  [1,puntosIniciales[1],-1],
  [1,puntosIniciales[2],1]]
)
n=np.matrix([[math.sin(-math.pi/64)],[math.sin(math.pi/128)],[math.sin(math.pi/64)]])
solucion=(m**-1)*n
print("solucion",solucion)
#construimos la nueva funcion polinomica de grado 1
def f(x):
  return (3.69567960e-06 + 9.99598453e-01*x)
#creamos el rango
x=np.arange(-math.pi/64,math.pi/64,0.0001)
#creamos un rango para la del seno
y=np.arange(-math.pi/64-0.1,math.pi/64+0.1,0.0001)
#Como los maximos y minimos siguien siendo iguales evaluamos |p-f| en ellos y tiene que dar igual que el tercer valor dado por solución de la ecuación lineal 

print("Minimo",math.sin(-math.pi/64)-f(-math.pi/64))
print("Máximo",math.sin(math.pi/64)-f(math.pi/64))
#como vemos en pantalla da el mismo valor

#imprimimos ambas funciones en una grafica
pyplot.plot(y,[math.sin(i) for i in y],"blue")
pyplot.plot(x,[f(i) for i in x],"green")
pyplot.axhline(0,color="black")
pyplot.axvline(0,color="black")
pyplot.xlim(-math.pi/64-0.1,math.pi/64+0.1)
# Limitar los valores de los ejes.
pyplot.savefig("Remez.png")