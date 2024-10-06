
import math



#CALCULADORA IMPEDANCIA CONDENSADOR EN CIRCUITO DE CORRIENTE ALTERNA
def condensador():
    print('Introduce la frecuencia en Hz')
    frecuencia = int(input())
    print('Introduce la capacidad en F')
    capacidad = int(input())
    impedancia = (1/(math.pi*2*frecuencia*capacidad))

    print (f'La impedancia del condensador es de {impedancia} ohm')

#CALCULADORA IMPEDANCIA BOBINA EN CIRCUITO DE CORRIENTE ALTERNA
def bobina ():
    print('Introduce la frecuencia en Hz')
    frecuencia = int(input())
    print ('Introduce el valor de la bobina en H')
    reactancia = int(input())
    impedancia= (math.pi*2*frecuencia*reactancia)
    print (f'La impedancia de la bobina es de {impedancia}ohm')

print ('Deseas conocer la impedancia de un condensador o de una bobina?')
print ('1- Condensador')
print ('2- Bobina')
seleccion = int(input())

if seleccion ==1:
    condensador()

if seleccion ==2:
    bobina()
