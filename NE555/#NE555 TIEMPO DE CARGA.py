#NE555 TIEMPO DE CARGA 

#TIEMPO DURACIÓN NE555 MONOESTABLE
def NE555_MONOESTABLE() :
 print ('Cúal es la capacidad del condensador en uF?')
 CapacidadCondensador = int(input())
 print ('Cúal es el valor de R1?')
 Resistencia_1 = int (input())
 Tiempo_Duracion = 1,1*Resistencia_1*CapacidadCondensador
 print(f'EL led durará encendido {Tiempo_Duracion}')


#TIEMPO DURACIÓN NE555 ASTABLE
def NE555_ASTABLE_SIN_POT():
 print ('Cúal es la capacidad del condensador (uF)')
 CapacidadCondensador = int(input())
 print ('Cúal es el valor de R1?')
 Resistencia_1 = int (input())
 print ('Cúal es el valor de R2?')
 Resistencia_2 = int (input())
 ResistenciaTotal = Resistencia_1 + Resistencia_2
 Tiempo_Duracion_1 = 0,7 *(ResistenciaTotal*CapacidadCondensador)
 Tiempo_Duracion_2 = 0,7*(Resistencia_2*CapacidadCondensador)
 print (f'El tiempo que dura el led 1 encendido es de {Tiempo_Duracion_1}')
 print (f'El tiempo que dura el led 2 encendido es de {Tiempo_Duracion_2}')


def NE555_ASTABLE_POT_VARIABLE():
 print ('Cúal es la capacidad del condensador (uF)?')
 CapacidadCondensador = int(input())
 print ('Cúal es el valor de R1')
 Resistencia_1 = int(input())
 print ('Cúal es el valor de la Resistencia Variable 1')
 Resistencia_Variable_1 = int(input())
 print ('Cúal es el valor de R2?')
 Resistencia_2 = int(input())
 print ('Cúal es el valor de la Resistencia Variable 2 ')
 Resistencia_Variable_2 = int(input())
 Tiempo_Duracion_1 = 0,7*(Resistencia_1*CapacidadCondensador*Resistencia_Variable_1*Resistencia_2*Resistencia_Variable_2)
 Tiempo_Duracion_3 = 0,7*(Resistencia_1*CapacidadCondensador*Resistencia_2)
 Tiempo_Duracion_2 = 0,7*(CapacidadCondensador*Resistencia_2*Resistencia_Variable_2)
 Tiempo_Duracion_4 = 0,7*(CapacidadCondensador*Resistencia_2)
 print (f'El tiempo máximo que dura el led 1 encendido es de {Tiempo_Duracion_1}')
 print (f'El tiempo mínimo que dura el led 1 encendido es de {Tiempo_Duracion_3}')
 print (f'El tiempo máximo que dura el led 2 encendido es de {Tiempo_Duracion_2}')
 print (f'El tiempo mínimo que dura el LED 2 encendido es de {Tiempo_Duracion_4}')
#INTRODUCCIÓN
print ('Bienvenido a la calculadora del tiempo de encendido de un led controlado por un NE555')
print ('Para que circuito deseas realizar los cálculos?')
print ('NE555 MONOESTABLE (1)')
print ('NE555 ASTABLE (2)')
Seleccion_Calculo = int(input())

if Seleccion_Calculo == 1:
 NE555_MONOESTABLE()

if Seleccion_Calculo == 2: 
 print ('NE555 ASTABLE con resistencia variable (1)')
 print ('NE555 ASTABLE sin resistencia variable (2)')
 seleccion_2 = int(input())
 if seleccion_2 == 1:
  NE555_ASTABLE_POT_VARIABLE()
 if seleccion_2 == 2:
  NE555_ASTABLE_SIN_POT()