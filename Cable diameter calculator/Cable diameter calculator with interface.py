#CABLE DIAMETER CALCULATOR WITH INTERACE
import tkinter as tk
window = tk.Tk(whit = 300)
Titulo = tk.Label (text = 'Calculadora del diametro de un cable', bg = 'Yellow')    
Titulo.pack()
Introduccion = tk.Label (text = 'Que valores tienes?')
Introduccion.pack()


def Intensidad():
   
    Etiqueta_Intensidad = tk.Label(text = 'Introduce aquí la intensidad que circula por el cable')
    Etiqueta_Intensidad.pack()
    Entrada_Intensidad = tk.Entry()
    Entrada_Intensidad.pack()
    Etiqueta_Longitud = tk.Label(text = 'Introduce aquí la longitud del cable')
    Etiqueta_Longitud.pack()
    Entrada_Longitud = tk.Entry()
    Entrada_Longitud.pack()

    def Calculo():
        Intensidad =  int(Entrada_Intensidad.get())
        Longitud =    int(Entrada_Longitud.get())
        Resistencia = 0.5/Intensidad
        Calculo_Seccion = ((0.017*Longitud)/Resistencia)
        Salida = tk.Label(text = f'Necesitas una sección de: {Calculo_Seccion} mm')
        Salida.pack()
    Boton = tk.Button (text = 'Calcular', command = Calculo)
    Boton.pack()

def Potencia_Voltaje():
    Etiqueta_Potencia = tk.Label(text = 'Introduce aquí la potencia que debe de circular por el cable')
    Etiqueta_Potencia.pack()
    Entrada_Potencia = tk.Entry()
    Entrada_Potencia.pack()
    Etiqueta_Longitud = tk.Label(text = 'Introduce aquí la longitud del cable en m')
    Etiqueta_Longitud.pack()
    Entrada_Longitud = tk.Entry()
    Entrada_Longitud.pack()
    Etiqueta_Voltaje = tk.Label (text = 'Introduce aquí la tensión en V')
    Etiqueta_Voltaje.pack()
    Entrada_Voltaje = tk.Entry()
    Entrada_Voltaje.pack()
    def Calcular():
        Potencia = int(Entrada_Potencia.get())
        Longitud = int(Entrada_Longitud.get())
        Voltaje = int(Entrada_Voltaje.get())
        Intensidad = Potencia/Voltaje
        Resistencia = 0.5/Intensidad
        Calculo_Seccion = ((0.017*Longitud)/Resistencia)
        Salida = tk.Label(text = f'Necesitas una sección de cable de {Calculo_Seccion}mm')
        Salida.pack()
    Calcular = tk.Button(text = 'Calcular', command = Calcular)


Eleccion_1 = tk.Button (text = 'Calcular seccion a partir de intensidad', command = Intensidad)
Eleccion_1.pack()

Eleccion_2 = tk.Button (text = 'Calcular seccion a partir de potencia y tensión', command = Potencia_Voltaje)
Eleccion_2.pack()
window.mainloop()

