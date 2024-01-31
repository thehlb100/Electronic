
#Rectificador onda completa para Phyton

Voltajefase1 = int
Voltajefase2 = int
pi = 3.14159

def calcularondacompleta () :
 print ("¿Cúal es el voltaje de la fase 1")
 Voltajefase1 = int(input())
 print ("¿Cúal es el voltaje de la fase 2")
 Voltajefase2 = int(input())
 print ("¿Cúal es la resistencia en ohm?")
 res = int(input())
 Vmaxfase1 =  Voltajefase1*1.4
 Vmaxfase2 =  Voltajefase2*1.4
 Vmeddiod = (2*(Vmaxfase2 - 0.7 ))/pi
 Imeddiod = Vmeddiod/res
 Vdiod = Imeddiod*res
 print("El Vmax de la fase 1 es =", Vmaxfase1)
 print("El Vmax de la fase 2 es =", Vmaxfase2)
 print ("El Veficaz de la fase 1 es =", Voltajefase1)
 print ("El Veficaz de la fase 2 es =", Voltajefase2)
 print ("El Vmed del diodo es =", Vmeddiod)
 print ("La intensidad media del diodo es =", Imeddiod)
 print ("El Voltaje del diodo es =", Vdiod)

calcularondacompleta()
