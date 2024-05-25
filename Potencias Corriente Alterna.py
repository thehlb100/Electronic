import tkinter as tk
import math
window =tk.Tk()
Título = tk.Label(text = 'Calculadora de potencias de corriente Alterna')
Título.pack()

def potencia_Aparente():
    texto_pActiva = tk.Label(text = 'Introduce aquó la potencia activa (W)')
    texto_pActiva.pack()
    entrada_pActiva = tk.Entry()
    entrada_pActiva.pack()
    texto_pReactiva = tk.Label(text = 'Introduce aquí la potencia reactiva (W)')    
    texto_pReactiva.pack()
    entrada_pReactiva = tk.Entry()
    entrada_pReactiva.pack()

    def calcular():
        pActiva = int(entrada_pActiva.get())
        pReactiva = int(entrada_pReactiva.get())
        pAparente = math.sqrt((pActiva**2)+(pReactiva**2))
        texto_Salida = tk.Label(text = f'La potencia aparente es de {pAparente}W')
        texto_Salida.pack()
    
    boton_Calcular = tk.Button(command = calcular, text = 'Calcular')
    boton_Calcular.pack()

def potencia_Activa():
    texto_Voltaje = tk.Label(text = 'Introduce el Voltaje en V')
    texto_Voltaje.pack()
    introduccion_Voltaje = tk.Entry()
    introduccion_Voltaje.pack()
    texto_Resistencia = tk.Label(text = 'Introduce aquí la resistencia en ohm')
    texto_Resistencia.pack()
    entrada_Resistencia = tk.Entry()
    entrada_Resistencia.pack()
    def calcular():
        voltaje = int(introduccion_Voltaje.get())
        resistencia = int(entrada_Resistencia.get())
        potencia = voltaje*resistencia
        salida = tk.Label(text = f'La potencia activa es de {potencia}W')
        salida.pack()
    boton_Calcular = tk.Button(text = 'Calcular', command = calcular)
    boton_Calcular.pack()


#INTRODUCCIÓN
seleccion_Activa = tk.Button(text = 'Potencia Activa', command = potencia_Activa)
seleccion_Activa.pack()

seleccion_Aparente = tk.Button(text = 'Potencia Aparente', command = potencia_Aparente)
seleccion_Aparente.pack()

window.mainloop()
