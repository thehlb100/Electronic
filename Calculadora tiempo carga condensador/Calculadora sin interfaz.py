
#CALCULADORA TIEMPO CARGA DE UN CONDENSADOR
print ('Bienvenido a la calculadora de tiempo de carga de un condensador')
print ('Cual es el valor de la resistencia en ohm?')
resistencia = int(input())
print ('Cual es el valor de la capacidad del condensador en F?')
Capacidad_Condensador = int(input())
Calculo = 5*resistencia*Capacidad_Condensador
print (f'El condensador tarda {Calculo}s en cargar')