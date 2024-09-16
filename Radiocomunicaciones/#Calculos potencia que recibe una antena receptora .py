#Calculos potencia que recibe una antena receptora 

from math import pi


print('Introduce la frecuencia en MHz')
frecuencia = float(input())

print ('Introduce la ganancia de la antena de la estación transmisora en dB')
ganancia_Transmisor = float(input())

print ('Introduce la ganancia de la antena de la estación receptora en dB')
ganancia_Receptor = float(input())

print ('Introduce la distancia entre las dos estaciones')
distancia = float(input())


print ('Introduce la potencia de transmisión')
potencia_Transmision = float(input())


#Cálculos
longitud_Onda  = (3*(10**8)/(frecuencia*(10**6))) #Longitud de onda en MHz

potencia_Recibida = (((longitud_Onda/ (4*pi*distancia) )**2)*ganancia_Transmisor*ganancia_Receptor)*potencia_Transmision



#Respuesta
print (f'La potencia_Recibida es de {potencia_Recibida}W ')