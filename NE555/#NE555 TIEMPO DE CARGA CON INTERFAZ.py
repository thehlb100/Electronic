#NE555 TIEMPO DE CARGA CON INTERFAZ
import tkinter as tk
ventana = tk.Tk()

# NE555 MONOESTABLE
def NE555_Monoestable():
    Texto_Capacidad_Condensador = tk.Label(text = 'Introduce la capacidad del condensador en uF')
    Entry_Capacidad_Condensador = tk.Entry()
    Texto_Capacidad_Condensador.pack()
    Entry_Capacidad_Condensador.pack()

    Texto_Resistencia_1 = tk.Label(text = 'Introduce el valor de la resistencia en Ohm')
    Entry_Resistencia_1 = tk.Entry()
    Texto_Resistencia_1.pack()
    Entry_Resistencia_1.pack()

    def Calcular_Tiempo():
        Capacidad_Condensador = int(Entry_Capacidad_Condensador.get())
        Resistencia_1 = int(Entry_Resistencia_1.get())
        Tiempo_Duracion = 1,1*Resistencia_1*Capacidad_Condensador
        Salida = tk.Label(text = f'El tiempo que el led estará encendido será de {Tiempo_Duracion}s')
        Salida.pack()

    Boton_Calcular = tk.Button(text = 'Calcular', command = Calcular_Tiempo)
    Boton_Calcular.pack()

#NE555 ASTABLE SIN POTENCIÓMETRO
def NE555_Sin_Pot():
    Texto_Capacidad_Condensador = tk.Label('Introduce la capacidad del condensador en uF')
    Entry_Capacidad_Condensador = tk.Entry()
    Texto_Capacidad_Condensador.pack()
    Entry_Capacidad_Condensador.pack()

    Texto_Resistencia_1 = tk.Label(text = 'Introduce el valor de la resistencia 1 en Ohm')
    Entry_Resistencia_1 = tk.Entry()
    Texto_Resistencia_1.pack()
    Entry_Resistencia_1.pack()

    Texto_Resistencia_2 = tk.Label(text = 'Introduce el valor de la resistencia 2 en Ohm')
    Entry_Resistencia_2 = tk.Entry()
    Texto_Resistencia_2.pack()
    Entry_Resistencia_2.pack()

    def calcular():
        Capacidad_Condensador = int(Entry_Capacidad_Condensador.get())
        Resistencia_1 = int(Entry_Resistencia_1.get())
        Resistencia_2 = int(Entry_Resistencia_2.get())
        Resistencia_Total = Resistencia_1 + Resistencia_2
        Tiempo_Duracion_1 = 0,7*(Resistencia_Total*Capacidad_Condensador)
        Tiempo_Duracion_2 = 0,7*(Resistencia_2*Capacidad_Condensador)
        Salida_1 = tk.Label(text = f'El LED 1 tendrá durará {Tiempo_Duracion_1}s encendido')
        Salida_2 = tk.Label(text = f'El LED 2 tendrá una durará {Tiempo_Duracion_2}s encendido')
        Salida_1.pack()
        Salida_2.pack()

    Boton_Calcular = tk.Button(text = 'Calcular', command = calcular)
    Boton_Calcular.pack()




def Elección():
    Título = tk.Label(text = 'NE555 - Calculator', bg = 'Green')
    Título.pack()


    Elegir_NE555_Monoestable = tk.Button (command = NE555_Monoestable, text = 'NE555_Monoestable')
    Elegir_NE555_Monoestable.pack()

    Elegir_NE555_Astable_Sin_Pot = tk.Button(command = NE555_Sin_Pot, text = 'NE555 Astable sin potenciómetro')
    Elegir_NE555_Astable_Sin_Pot.pack()



Elección()








ventana.mainloop()