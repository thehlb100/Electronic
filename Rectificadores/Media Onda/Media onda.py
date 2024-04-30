pi = 3.141516
print ("Cual es el voltaje de entrada?")
Voltajentrada = int(input ())
print ("Cual es el voltaje de salida del transformador?")
Voltajesalida = int (input ())
Vmaxin = Voltajentrada * 1.414
Vmaxs = Voltajesalida*1.414
Vmed = Vmaxs/pi
Vmed1 = Vmaxin/pi
print ("Cual es el valor de la resistencia RL?")
Res = int (input())
Imed = Vmed/Res
Vmeddiodo= (Vmaxs-0.7)/pi
Imeddiodo = Vmeddiodo/Res

print ("El voltaje máximo de entrada es =", Vmaxin)
print ("El voltaje máximo de salida es =" , Vmaxs)
print ("El voltaje medio de la saluda es =", Vmed)
print ("El voltaje medio de entrada es =", Vmed1)
print ("La intensidad media de la salida es =", Imed)
print ("El valor medio del diodo es =", Vmeddiodo)
print ("La intensidad media del diod es =", Imeddiodo)
