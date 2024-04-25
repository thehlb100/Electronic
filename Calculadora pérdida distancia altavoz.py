import tkinter as tk
import math
#CALCULADORA DE PÉRDIAS POR DISTANCIA ALTAVOCES
window =tk.Tk()
Título = tk.Label(text = 'Calculadora pérdias por distancia en altavoces')
Etiqueta_Distancia = tk.Label(text = 'Introduce aquí la distancia desde el altavoz')
Etiqueta_Distancia.pack()
Entrada_Distancia = tk.Entry()
Entrada_Distancia.pack()
Etiqueta_Potencia = tk.Label(text = 'Introduce aquí la potencia del altavoz')
Etiqueta_Potencia.pack()
Entrada_Potencia = tk.Entry()
Entrada_Potencia.pack()
Etiqueta_Db = tk.Label (text = 'Introduce aquí los dB')
Etiqueta_Db.pack()
Entrada_DB = tk.Entry()
Entrada_DB.pack()

def Calcular():
    Distancia = int(Entrada_Distancia.get())
    Potencia = int(Entrada_Potencia.get())
    Db = int(Entrada_DB.get())
    a = Db - 20*(math.log(Potencia, 10)) + 10*(math.log(Distancia,10))
    salida = tk.Label(text = f'La pérdida en dB es de: {int(a)} dB')
    salida.pack()
 
Activar_Calculo = tk.Button (text = 'Pulsa aquí', command = Calcular)
Activar_Calculo.pack()

window.mainloop()