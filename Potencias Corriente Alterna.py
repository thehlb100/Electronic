import tkinter as tk
window =tk.Tk()
Título = tk.Label(text = 'Calculadora de potencias de corriente Alterna')
Título.pack()


def Potencia_Activa():
    Texto_Voltaje = tk.Label(text = 'Introduce el Voltaje en V')
    Texto_Voltaje.pack()
    Introduccion_Voltaje = tk.Entry()
    Introduccion_Voltaje.pack()
    Texto_Resistencia = tk.Label(text = 'Introduce aquí la resistencia en ohm')
    Texto_Resistencia.pack()
    Entrada_Resistencia = tk.Entry()
    Entrada_Resistencia.pack()
    def Calcular():
        Voltaje = int(Introduccion_Voltaje.get())
        Resistencia = int(Entrada_Resistencia.get())
        Potencia = Voltaje*Resistencia
        Salida = tk.Label(text = f'La potencia activa es de {Potencia}W')
        Salida.pack()
    Boton_Calcular = tk.Button(text = 'Calcular', command = Calcular)
    Boton_Calcular.pack()

Potencia_Activa()
window.mainloop()
