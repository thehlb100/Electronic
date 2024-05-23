#CALCULADORA CIRCUITOS DE CORRIENTE ALTERNA 
import math
import tkinter as tk

window = tk.Tk()

#Calcular valor instantáneo
def valor_Instantaneo():
    window_valor_Instantaneo = tk.Tk()
    #Introducción de datos
    amplitud_V_Text = tk.Label(text = 'Introduce aquí la amplitud en V')
    amplitud_V_Entry = tk.Entry()

    tiempo_Periodo_Text = tk.Label(text = 'Introduce aquí el tiempo de un periodo')
    tiempo_Periodo_Entry = tk.Entry()

    tiempo_Onda_Text = tk.Label(text = 'Introduce el tiempo ')
    tiempo_Onda_Entry = tk.Entry()

    amplitud_V_Text.pack()
    amplitud_V_Entry.pack()

    tiempo_Periodo_Text.pack()
    tiempo_Periodo_Entry.pack()

    tiempo_Onda_Text.pack()
    tiempo_Onda_Entry.pack()

    #Cálculos
    def calcular_Valor_Instantaneo():
        amplitud_V = int(amplitud_V_Entry.get())
        tiempo_Onda = int(tiempo_Onda_Entry.get())
        tiempo_Periodo = int(tiempo_Periodo_Entry.get())

        frecuencia = 1/tiempo_Periodo
        w = 2*math.pi*frecuencia
        valor_Instantaneo = amplitud_V * math.sin(w*tiempo_Onda)
        salida = tk.Label(text = f'El valor instantáneo es {valor_Instantaneo}V' )
        salida.pack()

    #Boton calcular
    boton_Valor_Instantaneo = tk.Button (text = 'Calcular', command = calcular_Valor_Instantaneo)
    boton_Valor_Instantaneo.pack()
    window_valor_Instantaneo.mainloop()


boton_Valor_Instantaneo = tk.Button(text = 'Calculadora valor instantáneo', command = valor_Instantaneo)
boton_Valor_Instantaneo.pack()
window.mainloop()