from matplotlib import pyplot
def sumaCuadrados(n):
  tam= n**2
  sum=0
  i=1
  for i in range(tam+1):
    sum+= i**2
  return sum

x = range(0,10)
# Graficar ambas funciones.
pyplot.plot(x, [sumaCuadrados(i) for i in x],"red")
# Establecer el color de los ejes.
pyplot.axhline(0,color="black")
pyplot.axvline(0,color="black")
# Limitar los valores de los ejes.
pyplot.xlim(-10, 20)
pyplot.ylim(-10, 200000)
# Guardar gráfico como imágen PNG.
pyplot.savefig("SumaCuadrados.png")
# Mostrarlo.
pyplot.show()