#CALCULADORA
import tkinter as tk
#Creación ventana y título
window = tk.Tk()
Título = tk.Label(text = 'Calculadora de conceptos magnetismo', bg= 'Red')
Título.pack()


#Definición de los tipos de calculadoras
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

def Calculadora_Permeabilidad_Magnética():
    Texto_Flujo_Magnético = tk.Label(text = 'Introduce aquí el flujo magnético en Wb')
    Texto_Flujo_Magnético.pack()
    Entrada_Flujo_Magnético = tk.Entry()
    Entrada_Flujo_Magnético.pack()
    Texto_Intensidad_Campo = tk.Label(text = 'Introduce aquí la intensidad del campo mágnetico en A/Número de vueltas')
    Texto_Intensidad_Campo.pack()
    Entrada_Intensidad_Campo = tk.Entry()
    Entrada_Intensidad_Campo.pack()
    def Calcular():
        Flujo_Magnético = int(Entrada_Flujo_Magnético.get())
        Intensidad_Campo = int(Entrada_Intensidad_Campo)
        Permeabilidad_Magnética = Flujo_Magnético/Intensidad_Campo
        Salida = tk.Label(text = f'La permeabilidad magnética es de {Permeabilidad_Magnética}H/m')
        Salida.pack()
   
    Boton_Calcular = tk.Button(text = 'Calcular', command = Calcular)
    Boton_Calcular.pack()

def Calculadora_Intensidad_Campo():
    Texto_Longitud = tk.Label (text = 'Introduce la longitud en M')
    Texto_Longitud.pack()
    Entrada_Longitud = tk.Entry()
    Entrada_Longitud.pack()
    Texto_Número_Vueltas = tk.Label(text = 'Introduce aquí el número de vueltas de la bobina')
    Texto_Número_Vueltas.pack()
    Entrada_Número_Vueltas = tk.Entry()
    Entrada_Número_Vueltas.pack()
    Texto_Intensidad = tk.Label(text = 'Introduce aquí la intensidad en A')
    Texto_Intensidad.pack()
    Entrada_Intensidad = tk.Entry()
    Entrada_Intensidad.pack()
    def Calcular():
        Longitud = int(Entrada_Longitud.get())
        Número_Vueltas = int(Entrada_Número_Vueltas.get())
        Intensidad = int(Entrada_Longitud.get())
        Calculo = (Número_Vueltas*Intensidad)/Longitud
        Salida = tk.Label(text = f'La Intensidad de Campo es de {Calculo}A x vuelta/metro')
        Salida.pack()
    Boton_Calcular = tk.Button(text = 'Calcular', command = Calcular)
    Boton_Calcular.pack()


#Botones de elección de lo que se desea calcular

Introducción_Calculadora_Inducción = tk.Button (text = 'Calculadora_Inducción_Magnética', command = Calculadora_Inducción_Magnética)
Introducción_Calculadora_Inducción.pack()

Introducción_Calculadora_Permeabilidad_Magnética = tk.Button (text = 'Calculadora_Permeabilidad_Magnética', command = Calculadora_Permeabilidad_Magnética)
Introducción_Calculadora_Permeabilidad_Magnética.pack()

Introducción_Calculadora_Intensidad_Campo = tk.Button(text = 'Calculadora Intensidad de Campo', command = Calculadora_Intensidad_Campo)
Introducción_Calculadora_Intensidad_Campo.pack()

window.mainloop()
