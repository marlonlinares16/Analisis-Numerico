#Calculo del error de interpolaci?n
error<-function(x,f,s,n)
{
  err<-0
  sol<-0
  ans<-0
  for(i in 1:n)
  {
    h<-max(x[i+1]-x[i])
    err=h^(3/2)
    ans = f(x[i])-s[i]
    if(!is.null((ans< err))||!is.null((ans==err)))
    {
      sol[i]=ans
    }
  }
  return(sol)
}

#Imprime los resultados pertinentes
tabla<-function(x,y,err)
{
  datos<-data.frame(cbind(x,y,err))
  colnames(datos)<-c('X','Spline','Error')
  print(datos)
}

#Calculo del tama?o de paso "h"
#De la forma que h(i) = x(i+i) - x(i)
calHi<-function(x)
{
  n = length(x)
  h <- (c(x,0) - c(0,x))[2:n]
  return (h)
}

#Calculo de la matriz A que hace parte del sistema de ecuaciones As=B
#Es de la forma que cuando esta en la iteraci?n i
#Cuando (i,j) i = j = 2(hi+hi+1)
#Cuando (i,j-1) = hi
#Cuando (i,j+1) = hi+1
matrizA<-function(h,a,x)
{
  n = length(x)
  alph <- (3/c(1,h,1,1)*(c(a,1,1) - c(1,a,1)) - 3/c(1,1,h,1)*(c(1,a,1)-c(1,1,a)))[3:n]
  A <- c(1,rep(0,times=n-1))
  for (i in 1:(n-2)) {
    A <- rbind(A,c( rep(0,times=i-1) , c(h[i],2*(h[i]+h[i+1]),h[i+1]) , rep(0,times=n-i-2) ) )
  }
  A <- rbind(A,c(rep(0,times=n-1),1))

  return(A)
}

#Calculo de la matriz B que hace parte del sistema de ecuaciones As=B
#Es de la forma que cuando esta en la iteraci?n i
#Cuando (i,1) = 6((yi+2-yi+1)/hi+1-(yi+1-yi)/hi)
matrizB<-function(h,a,x)
{
  n = length(x)
  alph <- (3/c(1,h,1,1)*(c(a,1,1) - c(1,a,1)) - 3/c(1,1,h,1)*(c(1,a,1)-c(1,1,a)))[3:n]
  b <- c(0,alph,0)
  return (b)
}

#Despeje de la ecuaci?n de la forma AS=B en el cual obtenemos los valores de Spline
#que nos ayudar? a calcular los polinomios de interpolaci?n
calS<-function(A,b)
{
  c <- solve(A, b)
  return(c)
}

#Calculo de los coeficientes del polinomio de interpolaci?n Spline
#Recibe los spline del despeje de la ecuaci?n As=B
#los valores en X, Y y el tama?o de paso (h)
sNormal<-function(a,c,h,x)
{
  n = length(x)
  b <- ((c(a,0) - c(0,a))/c(1,h,1) - c(1,h,1)/3*(c(c,0) + 2*c(0,c)))[2:n]
  d <- ((c(c,0) - c(0,c))/(3*c(1,h,1)))[2:n]

  ans = rbind(a[1:n-1],b,c[1:n-1],d)
}

#Splie cubico, llama a las respectivas funciones para que la interpolacion funcione
sCubico<-function(x,y)
{
  h<-calHi(x)
  A<-matrizA(h,y,x)
  B<-matrizB(h,y,x)
  S<-calS(A,B)
  sNormal(y,S,h,x)
}

#Funcion que llama a las funciones de interpolar
#Graficar y calcular el error
splineCubico<-function(x,y)
{
  plot(x,y, pch=19, cex=1, col = "red", asp = 1, xlab="X", ylab = "Y", main = "Spline Cubico")
  f = splinefun(x,y,method = "natural", ties = mean)
  t = 1:length(x)
  sx = sCubico(t,x)
  sy = sCubico(t,y)
  for (i in 1:(length(t)-1)) {
    dat<- data.frame(t=seq(t[i],t[i+1], by=0.1) )
    fx <- function(x) (sx[1,i] + sx[2,i]*(x-t[i]) + sx[3,i]*(x-t[i])^2 + sx[4,i]*(x-t[i]))
    fy <- function(x) (sy[1,i] + sy[2,i]*(x-t[i]) + sy[3,i]*(x-t[i])^2 + sy[4,i]*(x-t[i]))
    dat$y=fy(dat$t)
    dat$x=fx(dat$t)
    points(dat$x,dat$y,type='l', col='blue')
    err=error(dat$x,f,dat$y,length(dat$x))
    tabla(dat$x,dat$y,err)
  }
}

x=c(1,2,5,6,7.5,8.1,10,13,17.6,20,23.5,24.5,25,26.5,27.5,28,29,30)
y=c(3,3.7,3.9,4.5,5.7,6.69,7.12,6.7,4.45,7,6.1,5.6,5.87,5.15,4.1,4.3,4.1,3)

x1=c(14.6, 14.7, 14.6, 14.8, 15.2, 15.6, 15.7, 17.0, 17.6, 17.5, 17.3, 16.8, 15.4, 14.8, 14.4, 14.5, 15.0, 15.1, 15.0, 14.9, 14.6, 14.3, 14.0, 13.9, 13.8, 13.5, 13.1, 13.0, 13.3, 13.2, 13.1, 12.9, 12.4, 11.9, 11.7, 11.6, 11.3, 10.9, 10.7, 10.6, 10.6, 10.1, 9.7, 9.4, 9.3, 9.6, 9.9, 10.1, 10.2, 10.3, 9.10, 8.6, 7.5, 7.0, 6.7, 6.6, 7.70, 8.00, 8.10, 8.40,              9.00, 9.30, 10, 10.2, 10.3, 10.0, 9.50)
y1=c(14.7, 14.0, 13.4, 12.3, 11.0, 10.5, 10.2, 8.20, 7.10, 6.70, 6.60, 6.80, 8.30, 8.80, 9.30, 8.80, 6.30, 5.50, 5.00, 4.70, 4.60, 4.50, 4.90, 5.40, 5.80, 6.90, 8.20, 7.60, 5.80, 4.50, 4.30, 3.90, 4.20, 5.70, 7.00, 7.90, 8.20, 7.30, 6.70, 5.50, 5.10, 4.60, 4.7, 5.0, 5.5, 7.2, 7.8, 8.60, 9.40, 10.0, 10.7, 9.9, 9.0, 9.1, 9.3, 9.7, 11.7, 12.3, 12.5, 13.0,              13.9, 14.9, 16, 16.4, 16.8, 10.7, 11.0)
splineCubico(x1,y1)
