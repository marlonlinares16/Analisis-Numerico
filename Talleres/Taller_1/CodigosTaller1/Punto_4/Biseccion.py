
from math import*
import numpy
from matplotlib import pyplot

#Metodo de la bisección

#funcion a probar
#entradas: un entero x
#salidas: un decimal 
def f2(x):
  return 4.26*x -0.0052*(x**3)
def f(x):
  y=6+2.13*(pow(x,2))
  y-=(0.0013*(pow(x,4)))
  return y
#funcion que representa el metodo de la biseccion 
#entradas: f la funcion a probar, a y b limites dados
#salidas: Xn donde f(x) de 0 
def metodobiseccion(f, x0, x1, e):
  while x1-x0>=e:
    x2=(x0+x1)/2 
    if f(x2)==0:
      return x2
    else:
      if f(x0)*f(x2)>0: 
        x0=x2
      else:
        x1=x2
  return x2

resultados=[]
x=numpy.arange(-50,50,0.1)
pyplot.plot(x, [f(i) for i in x],"blue")
pyplot.plot(x, [f2(i) for i in x],"green")

# Establecer el color de los ejes.
pyplot.axhline(0,color="black")
pyplot.axvline(0,color="black")
# Limitar los valores de los ejes.
pyplot.xlim(0, 50)
pyplot.ylim(0,1000)
# Guardar gráfico como imágen PNG.
pyplot.savefig("biseccion.png")
# Mostrarlo.
pyplot.show()

print(metodobiseccion(f2,25,35,0.0001))
print(f2(28.622207641601562))
print(f(28.622207641601562))