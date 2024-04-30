import tkinter as tk

window =tk.Tk()

#ENTRADAS DE DATOS
Etiqueta_Valor_Resistencia = tk.Label (text='Introduce aquí el valor de la resistencia', bg = 'Orange')
Etiqueta_Valor_Resistencia.pack()
Entrada_Resistencia = tk.Entry()
Entrada_Resistencia.pack()
Etiqueta_Valor_Condensador = tk.Label(text = 'Escribe aquí el Valor del Condensador', bg ='Yellow')
Etiqueta_Valor_Condensador.pack()
Entrada_Valor_Condensador = tk.Entry(text = 'Introduce aquí el valor del condensador')
Entrada_Valor_Condensador.pack()
Salida_Valor_Eficaz = tk.Label(text = 'El tiempo de carga es:')

#CÁLCULO TIEMPO DE CARGA 
def upd_1(eve):
    Salida_Valor_Eficaz['text'] =  Salida_Valor_Eficaz['text'] + str(int(Entrada_Resistencia.get())*(int(eve.char)*5) )
Entrada_Valor_Condensador.bind("<Key>", upd_1)

Salida_Valor_Eficaz.pack()

window.mainloop()

