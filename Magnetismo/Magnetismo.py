#CALCULADORA
import tkinter as tk
from tkinter import ttk
#Creación ventana y título
window = tk.Tk()
Título = tk.Label(text = 'Calculadora de conceptos magnetismo', bg= '#A8F5DD')
Título.pack()


#Definición de los tipos de calculadoras
def Calculadora_Inducción_Magnética():
    #Introducción de datos
    Texto_Flujo_Magnético = ttk.Label(text = 'Introduce aquí el flujo magnético en Wb')
    Texto_Flujo_Magnético.pack()
    Entrada_Flujo_Magnético = ttk.Entry()
    Entrada_Flujo_Magnético.pack()
    

    #Superficie
    Texto_Superficie = ttk.Label(text = 'Introduce aquí la superficie en m2')
    Texto_Superficie.pack()
    Entrada_Superficie = ttk.Entry ()
    Entrada_Superficie.pack()

    def Calcular():
        Flujo_Magnético = int(Entrada_Flujo_Magnético.get())
        Superficie = int(Entrada_Superficie.get())
        Inducción_Magnética = Flujo_Magnético/Superficie
        Salida = ttk.Label(text = f'La inducción magnética es de {Inducción_Magnética}T')
        Salida.pack()

    Boton_Calcular = ttk.Button(text = 'Calcular', command = Calcular)
    Boton_Calcular.pack()

def Calculadora_Permeabilidad_Magnética():
    Texto_Flujo_Magnético = ttk.Label(text = 'Introduce aquí el flujo magnético en Wb')
    Texto_Flujo_Magnético.pack()
    Entrada_Flujo_Magnético = ttk.Entry()
    Entrada_Flujo_Magnético.pack()
    Texto_Intensidad_Campo = ttk.Label(text = 'Introduce aquí la intensidad del campo mágnetico en A/Número de vueltas')
    Texto_Intensidad_Campo.pack()
    Entrada_Intensidad_Campo = ttk.Entry()
    Entrada_Intensidad_Campo.pack()
    def Calcular():
        Flujo_Magnético = int(Entrada_Flujo_Magnético.get())
        Intensidad_Campo = int(Entrada_Intensidad_Campo)
        Permeabilidad_Magnética = Flujo_Magnético/Intensidad_Campo
        Salida = ttk.Label(text = f'La permeabilidad magnética es de {Permeabilidad_Magnética}H/m')
        Salida.pack()
   
    Boton_Calcular = ttk.Button(text = 'Calcular', command = Calcular)
    Boton_Calcular.pack()

def Calculadora_Intensidad_Campo():
    Texto_Longitud = ttk.Label (text = 'Introduce la longitud en M')
    Texto_Longitud.pack()
    Entrada_Longitud = ttk.Entry()
    Entrada_Longitud.pack()
    Texto_Número_Vueltas = ttk.Label(text = 'Introduce aquí el número de vueltas de la bobina')
    Texto_Número_Vueltas.pack()
    Entrada_Número_Vueltas = ttk.Entry()
    Entrada_Número_Vueltas.pack()
    Texto_Intensidad = ttk.Label(text = 'Introduce aquí la intensidad en A')
    Texto_Intensidad.pack()
    Entrada_Intensidad = ttk.Entry()
    Entrada_Intensidad.pack()
    def Calcular():
        Longitud = int(Entrada_Longitud.get())
        Número_Vueltas = int(Entrada_Número_Vueltas.get())
        Intensidad = int(Entrada_Longitud.get())
        Calculo = (Número_Vueltas*Intensidad)/Longitud
        Salida = ttk.Label(text = f'La Intensidad de Campo es de {Calculo}A x vuelta/metro')
        Salida.pack()
    Boton_Calcular = ttk.Button(text = 'Calcular', command = Calcular)
    Boton_Calcular.pack()

def Calculadora_Inductancia():
    Texto_Numero_Espiras = ttk.Label(text = 'Introduce aquí el número de espiras de la bobina')
    Texto_Numero_Espiras.pack()
    Entrada_Numero_Espiras = ttk.Entry()
    Entrada_Numero_Espiras.pack()
    Texto_Intensidad = ttk.Label(text = 'Introduce aquí la intensidad en A')
    Texto_Intensidad.pack()
    Entrada_Intensidad = ttk.Entry()
    Entrada_Intensidad()
    Texto_Flujo_Magnético = ttk.Label(text = 'Introduce aquí el flujo magnético en Wb')
    Texto_Flujo_Magnético.pack()
    Entrada_Flujo_Magnético = ttk.Entry()
    Entrada_Flujo_Magnético.pack()
    def Calcular():
        Numero_Espiras = int(Entrada_Numero_Espiras.get())
        Intensidad = int(Entrada_Intensidad.get())
        Flujo_Magnético = int(Entrada_Flujo_Magnético.get())
        Operación = (Numero_Espiras*Flujo_Magnético)/Intensidad
        Salida = ttk.Label(text = f'La inductancia es de {Operación}H')
        Salida.pack()
    Boton = ttk.Button(text = 'Calcular', command = Calcular)
    Boton.pack()

#Botones de elección de lo que se desea calcular

Introducción_Calculadora_Inducción = ttk.Button (text = 'Calculadora_Inducción_Magnética', command = Calculadora_Inducción_Magnética)
Introducción_Calculadora_Inducción.pack()

Introducción_Calculadora_Permeabilidad_Magnética = ttk.Button (text = 'Calculadora_Permeabilidad_Magnética', command = Calculadora_Permeabilidad_Magnética)
Introducción_Calculadora_Permeabilidad_Magnética.pack()

Introducción_Calculadora_Intensidad_Campo = ttk.Button(text = 'Calculadora Intensidad de Campo', command = Calculadora_Intensidad_Campo)
Introducción_Calculadora_Intensidad_Campo.pack()

Intoducción_Calculadora_Inductancia = ttk.Button(text = 'Calculadora de Inductancia de una bobina', command = Calculadora_Inductancia)
Intoducción_Calculadora_Inductancia.pack()

window.mainloop()
