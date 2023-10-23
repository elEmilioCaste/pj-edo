#!/usr/bin/python

#Juan Carlos Espinosa Ceniceros
#ITS-FIME-UANL
#Agosto 2012
#Automatizacion y Control
import curses

def funcion(x, y):
    return (2*(x*y))

def rungeKutta(h, x0, y0):
    x = x0 + h
    k1 = h * funcion(x0, y0)
    k2 = h * funcion(x0 + (h/2), y0 + (k1/2))
    k3 = h * funcion(x0 + (h/2), y0 + (k2/2))
    k4 = h * funcion(x0 + h, y0 + k3)
    pendiente = (k1 + 2*k2 + 2*k3 + k4)/6
    y = y0 + pendiente
    return [x, y, k1, k2, k3, k4, pendiente]

def main():
    yAprox = float(curses.raw_input("Aproximar 'y' a << "))
    h = float(curses.raw_input("Tamano paso (h) << "))
    y0 = float(curses.raw_input("y0 << "))
    x0 = float(curses.raw_input("x0 << "))
    
    iteracion = 0
    while(x0 < yAprox):
        resultadoIteracion = rungeKutta(h, x0, y0)
        iteracion += 1
        print ("==================================")
        print ("Iteracion %d\n" %(iteracion))
        print ("K1   = %f" %(resultadoIteracion[2]))
        print ("K2   = %f" %(resultadoIteracion[3]))
        print ("K3   = %f" %(resultadoIteracion[4]))
        print ("K4   = %f" %(resultadoIteracion[5]))
        print ("X(%d) = %f"  %(iteracion, resultadoIteracion[0]))
        print ("Y(%d) = %f" %(iteracion, resultadoIteracion[1]))
        print ("==================================")
    
        y0 = resultadoIteracion[1]
        x0 = resultadoIteracion[0]

if(__name__ == "__main__"):
    main()