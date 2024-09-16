#NE555 TIEMPO DE CARGA CON INTERFAZ
import tkinter as tk
# NE555 MONOESTABLE
ventana = tk.Tk()


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




def Elección():
    Título = tk.Label(text = 'NE555 - Calculator', bg = 'Green')
    Título.pack()


    Elegir_NE555_Monoestable = tk.Button (command = NE555_Monoestable, text = 'NE555_Monoestable')
    Elegir_NE555_Monoestable.pack()



Elección()





ventana.mainloop()