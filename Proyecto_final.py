import tkinter as tk
from tkinter import *
import numpy as np                                                  #este hay que instalarlo con pip
import matplotlib                                                   #este hay que instalarlo con pip
from tkinter import Canvas, Label, Button, Entry, Checkbutton, Text, ttk
from PIL import ImageTk, Image
from sympy import sin, cos, sympify, lambdify                       #este hay que instalarlo con pip
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class RungeKuttaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1000x500')
        self.title('Método de Runge-Kutta')
        self.canvas = Canvas(self, width=1000, height=500)
        self.canvas.place(x=0, y=0)
        img = Image.open("fondo.jpg")
        img = ImageTk.PhotoImage(img)
        self.canvas.create_image(500, 250, anchor="center", image=img)
        #------------------------------------------------Textos---------------------------------------------------------
        self.canvas.create_text(50, 23, text="Runge-Kutta", anchor="nw", font=("Arial", 25, "bold"), fill='#fff')
        self.canvas.create_text(85,95,text="Ingrese la ecuación:", anchor="nw", font=("Arial", 10, "bold"))
        self.canvas.create_text(50,115,text="Y' = ", anchor="nw", font=("Arial", 10, "bold"))
        self.canvas.create_text(805,95,text="Ingrese los valores Iniciales:", anchor="nw", font=("Arial", 10, "bold"))
        self.canvas.create_text(815,120,text="Xo =", anchor="nw", font=("Arial", 10, "bold"))
        self.canvas.create_text(815,145,text="Yo =", anchor="nw", font=("Arial", 10, "bold"))
        self.canvas.create_text(825,165,text="Valor a Calcular y(x)", anchor="nw", font=("Arial", 10, "bold"))
        self.canvas.create_text(825,190,text="X =", anchor="nw", font=("Arial", 10, "bold"))
        self.canvas.create_text(825,209,text="Paso", anchor="nw", font=("Arial", 10, "bold"))
        self.canvas.create_text(825,234,text="h =", anchor="nw", font=("Arial", 10, "bold"))
        self.canvas.create_text(815,259,text="Aproximación a mostrar:", anchor="nw", font=("Arial", 10, "bold"))
        #-------------------------------------------------Entrys-------------------------------------------------------
        self.tbx1 = Entry(self) #-------Ingreso de Ecuacion-------
        self.tbx1.place(x=85,y=115)
        self.tbx2 = Entry(self)#----------------X_o---------------
        self.tbx2.place(x=850,y=118)
        self.tbx3 = Entry(self)#----------------Y_o---------------
        self.tbx3.place(x=850,y=143)
        self.tbx4 = Entry(self)#-----------------X----------------
        self.tbx4.place(x=850,y=187)
        self.tbx5 = Entry(self)#-----------------h----------------
        self.tbx5.place(x=850,y=231)
        self.txt = Text(self, width=40, height=20)
        self.txt.place(x=45, y=145)
        #------------------------------------------------Graficador-----------------------------------------------------
        self.cv2 = Canvas(self, width=300, height=319)
        self.cv2.place(x=450, y=145)
        #-----------------------------------------------CheckButtons----------------------------------------------------
        var = tk.IntVar()
        self.cbt1 = Checkbutton(self, text="RK1",background="#EB5C18",command=lambda: [self.cbt2.deselect(), self.cbt3.deselect()])
        self.cbt1.place(x=825,y=274)
        self.cbt2 = Checkbutton(self, text="RK2",background="#EB5C18",command=lambda: [self.cbt1.deselect(), self.cbt3.deselect()])
        self.cbt2.place(x=825,y=294)
        self.cbt3 = Checkbutton(self, text="RK4",background="#EB5C18",command=lambda: [self.cbt1.deselect(), self.cbt2.deselect()])
        self.cbt3.place(x=825,y=314)
        #-----------------------------------------------Buttons----------------------------------------------------
        self.b1 = Button(self, text="Calcular", width=10, command=lambda: evaluar(self, self.tbx1, self.tbx2, self.tbx3, self.tbx4, self.tbx5, self.cbt1, self.cbt2, self.cbt3))
        self.b1.place(x=850,y=344)
        self.b2 = Button(self, text="Cerrar", width=10, command=self.destroy)
        self.b2.place(x=850,y=374)
        #--------------------------------------------------------------------------------------------------------------
        self.mainloop()









#Funcion que manda a ejecutar los metodos RK
def evaluar(self, tbx1, tbx2, tbx3, tbx4, tbx5, cbt1, cbt2, cbt3):
    """if cbt1.state():
        print("sacar el 1")
    elif cbt2.variable:
        print("sacar el 2")
    elif cbt3.variable:
        print("sacar el 4")
    else: print("jajaja")"""


    
    self.frm = Frame(self)

    self.tabla = ttk.Treeview(self.frm, height=14)

    self.tabla['columns'] = ('Xn', 'RK1', 'RK2', 'RK4')

    self.tabla.column("#0", width=0,  stretch=NO)
    self.tabla.column("Xn",anchor=CENTER, width=80)
    self.tabla.column("RK1",anchor=CENTER,width=81)
    self.tabla.column("RK2",anchor=CENTER,width=81)
    self.tabla.column("RK4",anchor=CENTER,width=81)

    self.tabla.heading("#0",text="",anchor=CENTER)
    self.tabla.heading("Xn",text="Xn",anchor=CENTER)
    self.tabla.heading("RK1",text="RK1",anchor=CENTER)
    self.tabla.heading("RK2",text="RK2",anchor=CENTER)
    self.tabla.heading("RK4",text="RK4",anchor=CENTER)


    
    #obtener los datos
    ecu = tbx1.get()
    x0 = float(tbx2.get())
    y0 = float(tbx3.get())
    valF = float(tbx4.get())
    h = float(tbx5.get())
    iterTimes = int(valF / h)

    #arreglos para la tabla
    filaTabla = ['{:.4f}'.format(x0),'{:.4f}'.format(y0),'{:.4f}'.format(y0),'{:.4f}'.format(y0)]
    self.tabla.insert(parent='',index='end',iid=0,text='',values= filaTabla)

    #limpiar los entrys
    tbx1.delete(0, len(tbx1.get()))
    tbx2.delete(0, len(tbx2.get()))
    tbx3.delete(0, len(tbx3.get()))
    tbx4.delete(0, len(tbx4.get()))
    tbx5.delete(0, len(tbx5.get()))

    #establecemos los valores base
    x = x0
    y1 = y0
    y2 = y0
    y4 = y0
    #evaluar RK

    print('{:.4f}'.format(x0), " -> ", '{:.4f}'.format(y0))
    x = x + h
    #hacemos las iteraciones del metodo RK
    for i in range(iterTimes):
        filaTabla[0] = '{:.4f}'.format(x)
        y_k1_1 = RK1Step(ecu, h, x, y1)
        print('{:.4f}'.format(x), " 1 -> ", '{:.4f}'.format(y_k1_1))
        y1 = y_k1_1
        filaTabla[1] = '{:.4f}'.format(y1)

        y_k1_2 = RK2Step(ecu, h, x, y2)
        print('{:.4f}'.format(x), " 2 -> ", '{:.4f}'.format(y_k1_2))
        y2 = y_k1_2
        filaTabla[2] = '{:.4f}'.format(y2)

        y_k1_4 = RK4Step(ecu, h, x, y4)
        print('{:.4f}'.format(x), " 4 -> ", '{:.4f}'.format(y_k1_4))
        y4 = y_k1_4
        filaTabla[3] = '{:.4f}'.format(y4)
        
        self.tabla.insert(parent='',index='end',iid=i+1,text='',values= filaTabla)

        x = x + h

    self.frm.place(x=45,y=145)
    self.tabla.pack()





#Runge-Kutta de orden 1 que recibe: la funcion, x y t actuales, y el valor de paso
def RK1Step(foo, h, x, y):
    y_k1 = y + h * eval(foo)
    return y_k1

#Runge-Kutta de orden 2 que recibe: la funcion, x y t actuales, y el valor de paso
def RK2Step(foo, h, x, y):
    x_k = x
    y_k = y
    y = y_k + h/2 * eval(foo)
    x = x_k + h/2
    y_k1 = y_k + h * eval(foo)
    return y_k1

#Runge-Kutta de orden 4 que recibe: la funcion, x y t actuales, y el valor de paso
def RK4Step(foo, h, x, y):
    x_k = x
    y_k = y
    f_1 = eval(foo)
    y = y_k + h/2 * f_1
    x = x_k + h/2
    f_2 = eval(foo)
    y = y_k + h/2 * f_2
    f_3 = eval(foo)
    y = y_k + h * f_3
    x = x_k + h
    f_4 = eval(foo)
    y_k1 = y_k + h/6 * (f_1 + 2*f_2 + 2*f_3 + f_4)
    return y_k1

if __name__ == "__main__":
    app = RungeKuttaApp()