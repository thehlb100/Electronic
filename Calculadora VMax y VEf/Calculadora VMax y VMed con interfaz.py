import tkinter as tk

window =tk.Tk()

#CALCULADORA VALOR EFICAZ
label = tk.Label(text = 'Escribe aquí el Valor Eficaz', bg= "Red")    
entry = tk.Entry(width = 200)
label.pack()
entry.pack()    
label_1 = tk.Label(text = f'El Vmax es: ')
def upd(eve):
    label_1["text"] = label_1['text']+ str(int(eve.char)*1.4142)
entry.bind("<Key>", upd)
label_1.pack()

#CALCULADORA VALOR MÁXIMO
Entrada_Valor_Eficaz = tk.Entry()
Etiqueta_Valor_Eficaz = tk.Label(text = 'Escribe aquí el Valor Máximo', bg ='Yellow')
Etiqueta_Valor_Eficaz.pack()
Entrada_Valor_Eficaz.pack()
Salida_Valor_Eficaz = tk.Label(text = 'El valor eficaz es:')
def upd_1(eve):
    Salida_Valor_Eficaz['text'] =  Salida_Valor_Eficaz['text'] + str(int(eve.char)/1.414)
Entrada_Valor_Eficaz.bind("<Key>", upd_1)
Salida_Valor_Eficaz.pack()
window.mainloop()






