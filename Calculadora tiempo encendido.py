#CALCULADORA DE TIEMPO ENCENDIDO
print ("Cual es la resistencia total (ohm)?")
ResistenciaTotal= int(input())
print ("Cual es la capacidad del condensador (F)?")
CapacidadCondensador = int(input())
tiempo = 1,1 * ResistenciaTotal * CapacidadCondensador


print (f'El led durara {tiempo}s encendido')