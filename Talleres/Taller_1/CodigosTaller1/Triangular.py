
from matplotlib import pyplot
import random

def triangular(n):
  n=n+1
  constantes=[]
  coeficientes=[]
  contador=0
  for i in range(0,n):
    constantes.append(random.randrange(1,10))
  for i in range(0,n):
    aux=[]
    for j in range(n):
      aux.append(random.randrange(1,10))
    coeficientes.append(aux)
  tam=len(constantes)
  resultado=[];
  for i in range(0,tam):
    sum=0
    for j in range(0,i):
      sum=sum+coeficientes[i][j]*resultado[j] 
      contador+=1
    resultado=resultado+[(constantes[i]-sum)/coeficientes[i][i]]  
  return contador
x = range(0,100)
# Graficar ambas funciones.
pyplot.plot(x, [triangular(i) for i in x],"red")
# Establecer el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")
# Limitar los valores de los ejes.
pyplot.xlim(-10, 50)
pyplot.ylim(-100, 1000)
# Guardar gráfico como imágen PNG.
pyplot.savefig("output.png")
# Mostrarlo.
pyplot.show()