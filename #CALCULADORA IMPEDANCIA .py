#CALCULADORA DE IMPEDANCIAS
import math

#CALCULADORA IMPEDANCIA CIRCUITO CONDENSADOR Y RESISTENCIA
def circuito_RC():
    print('Introduce el valor de la resistencia en ohm')
    resistencia = float(input())
    print('Introduce la frecuencia en Hz')
    frecuencia = float(input())
    print('Introduce la capacidad del condensador en F')
    capacidad = float(input())
    impedancia_Condensador = (1/(math.pi*2*frecuencia*capacidad))
    impedancia_Total = math.sqrt((resistencia**2)-(impedancia_Condensador**2))
    print (f'La impedancia total del circuito es de {impedancia_Total}ohm')

#CALCULADORA IMPEDANCIA CONDENSADOR EN CIRCUITO DE CORRIENTE ALTERNA
def condensador():
    print('Introduce la frecuencia en Hz')
    frecuencia = float(input())
    print('Introduce la capacidad en F')
    capacidad = float(input())
    impedancia = (1/(math.pi*2*frecuencia*capacidad))
    print (f'La impedancia del condensador es de {impedancia} ohm')

#CALCULADORA IMPEDANCIA BOBINA EN CIRCUITO DE CORRIENTE ALTERNA
def bobina ():
    print('Introduce la frecuencia en Hz')
    frecuencia = float(input())
    print ('Introduce el valor de la bobina en H')
    reactancia = float(input())
    impedancia= (math.pi*2*frecuencia*reactancia)
    print (f'La impedancia de la bobina es de {impedancia}ohm')


#SELECCIONADOR E INTRO
print ('Bienvenido a la calculadora de impedancias!')
print ('Deseas conocer la impedancia de un condensador o de una bobina?')
print ('1- Condensador')
print ('2- Bobina')
print ('3- Circuito RC')
seleccion = int(input())

if seleccion ==1:
    condensador()

if seleccion ==2:
    bobina()

if seleccion ==3:
    circuito_RC()
