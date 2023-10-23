#Runge-Kutta de orden 1 que recibe: la funcion, x y t actuales, y el valor de paso
def RK1Step(foo, h, x_k, y_k):
    y_k1 = y_k + h * foo(x_k, y_k)
    return y_k1

#Runge-Kutta de orden 2 que recibe: la funcion, x y t actuales, y el valor de paso
def RK2Step(foo, h, x_k, y_k):
    y_k1 = y_k + h * foo(x_k + h/2, y_k + h/2 * foo(x_k, y_k))
    return y_k1

def RK4Step(foo, h, x_k, y_k):
    f_1 = foo(x_k, y_k)
    f_2 = foo(x_k + h/2, y_k + h/2 * f_1)
    f_3 = foo(x_k + h/2, y_k + h/2 * f_2)
    f_4 = foo(x_k + h, y_k + h * f_3)
    y_k1 = y_k + h/6 * (f_1 + 2*f_2 + 2*f_3 + f_4)
    return y_k1


def dump(x, y):
    ret = x+2-y
    return ret

def main():
    x0 = float(0)
    y0 = float(0)
    finX = float(1)
    h = 0.2
    iterTimes = int(finX / h)

    print("RK1----------------------")
    #imprimimos el caso base donde x0 = 0 y sumamos x0+h para seguir con la pimera iteracion
    print(x0, " -> ", '{:.4f}'.format(y0))
    x0 = x0 + h

    #hacemos las iteraciones del metodo RK
    for i in range(iterTimes):
        y_k1 = RK1Step(dump, h, x0, y0)
        print(x0, " -> ", '{:.4f}'.format(y_k1))
        y0 = y_k1
        x0 = x0 + h
    
    
    
    x0 = float(0)
    y0 = float(0)
    finX = float(1)
    h = 0.2
    iterTimes = int(finX / h)

    print("\n\nRK2----------------------")
    #imprimimos el caso base donde x0 = 0 y sumamos x0+h para seguir con la pimera iteracion
    print(x0, " -> ", '{:.4f}'.format(y0))
    x0 = x0 + h

    #hacemos las iteraciones del metodo RK
    for i in range(iterTimes):
        y_k1 = RK2Step(dump, h, x0, y0)
        print(x0, " -> ", '{:.4f}'.format(y_k1))
        y0 = y_k1
        x0 = x0 + h
    
    
    
    x0 = float(0)
    y0 = float(0)
    finX = float(1)
    h = 0.2
    iterTimes = int(finX / h)

    print("\n\nRK4----------------------")
    #imprimimos el caso base donde x0 = 0 y sumamos x0+h para seguir con la pimera iteracion
    print(x0, " -> ", '{:.4f}'.format(y0))
    x0 = x0 + h

    #hacemos las iteraciones del metodo RK
    for i in range(iterTimes):
        y_k1 = RK4Step(dump, h, x0, y0)
        print(x0, " -> ", '{:.4f}'.format(y_k1))
        y0 = y_k1
        x0 = x0 + h

main()


