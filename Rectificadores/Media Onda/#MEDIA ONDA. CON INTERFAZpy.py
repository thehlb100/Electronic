#MEDIA ONDA 
import tkinter as tk
window = tk.Tk()
window.pack()
pi = 3.141516

Introducción = tk.Label(text = 'Calculadora Media Onda')
Introducción.pack()

#INTRODUCCION DE DATOS
Introducción_Voltaje_Entrada = tk.Label(text = 'Introduce aquí el voltaje de entrada')
Introducción_Voltaje_Entrada.pack()
Voltaje_Entrada_Entry = tk.Entry()
Voltaje_Entrada_Entry.pack()
Introducción_Voltaje_Salida = tk.Label(text = 'Introduce aquí el voltaje de salida')
Introducción_Voltaje_Salida.pack()
Voltaje_Salida_Entry = tk.Entry()
Voltaje_Salida_Entry.pack()
Introducción_Resistencia = tk.Label (text = 'Introduce aquí el valor de RL')
Introducción_Resistencia.pack()
Resistencia_Entry = tk.Entry()
Resistencia_Entry.pack()

#CAMBIO DE INTRODUCCIÓN DE DATOS A INT
Voltaje_Entrada = int(Voltaje_Entrada_Entry.get())
Voltaje_Salida = int(Voltaje_Salida_Entry.get())
Resistencia = int(Resistencia_Entry.get())


#CALCULOS
Voltaje_Máximo_Entrada = Voltaje_Entrada*1.414
Voltaje_Máximo_Salida = Voltaje_Salida*1.414
Voltaje_Medio_Salida = Voltaje_Máximo_Salida/pi
Voltaje_Medio_Entrada = Voltaje_Máximo_Entrada/pi
Intensidad_Media = Voltaje_Medio_Salida/Resistencia
Voltaje_Medio_Diodo = (Voltaje_Máximo_Salida - 0.7)/pi
Intensidad_Media_Diodo = Voltaje_Medio_Diodo/Resistencia

#SALIDA
Salida_Voltaje_Máximo_Entrada = tk.Label(text = f'El voltaje máximo de entrada es {Voltaje_Salida}V')
Salida_Voltaje_Máximo_Entrada.pack()
Salida_Voltaje_Máximo_Salida = tk.Label (text = f'El voltaje máximo de saldia es de {Voltaje_Máximo_Salida}V')
Salida_Voltaje_Máximo_Salida.pack()
Salida_Voltaje_Medio_Salida = tk.Label(text = f'El voltaje medio a la salida es de {Voltaje_Medio_Salida}V')
Salida_Voltaje_Medio_Salida.pack()
Salida_Voltaje_Medio_Entrada = tk.Label(text = f'El voltaje medio de entrada es de {Voltaje_Medio_Entrada}V')
Salida_Intensidad_Media = tk.Label(text = f'La intensidad media de la saldia es de {Intensidad_Media}A')
Salida_Intensidad_Media.pack()
Salida_Voltaje_Medio_Diodo = tk.Label (text = f'El voltaje medio del diodo es {Voltaje_Medio_Diodo}V')
Salida_Voltaje_Medio_Diodo.pack()
Salida_Intensidad_Media_Diodo = tk.Label (text = f'La intensidad media del diodo es de {Intensidad_Media_Diodo}A')
Salida_Intensidad_Media_Diodo.pack()

window.mainloop()