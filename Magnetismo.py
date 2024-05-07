#CALCULADORA
import tkinter as tk
#Creación ventana y título
window = tk.Tk()
Título = tk.Label(text = 'Calculadora de conceptos magnetismo', bg= 'Red')
Título.pack()

def Calculadora_Inducción_Magnética():
    #Introducción de datos
    Texto_Flujo_Magnético = tk.Label(text = 'Introduce aquí el flujo magnético en Wb')
    Texto_Flujo_Magnético.pack()
    Entrada_Flujo_Magnético = tk.Entry()
    Entrada_Flujo_Magnético.pack()
    

    #Superficie
    Texto_Superficie = tk.Label(text = 'Introduce aquí la superficie en m2')
    Texto_Superficie.pack()
    Entrada_Superficie = tk.Entry ()
    Entrada_Superficie.pack()

    def Calcular():
        Flujo_Magnético = int(Entrada_Flujo_Magnético.get())
        Superficie = int(Entrada_Superficie.get())
        Inducción_Magnética = Flujo_Magnético/Superficie
        Salida = tk.Label(text = f'La inducción magnética es de {Inducción_Magnética}T')
        Salida.pack()

    Boton_Calcular = tk.Button(text = 'Calcular', command = Calcular)
    Boton_Calcular.pack()

Calculadora_Inducción_Magnética()

window.mainloop()
