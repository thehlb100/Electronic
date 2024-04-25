#CABLE DIAMETER CALCULATOR
def Intensidad_Voltaje():
 print ('Cuanta intensidad debe de circular por el cable?')
 Intensidad = int(input())
 print ('Cúal es la longitud del cable?')
 Longitud = int(input())
 print ('Cúal es el voltaje que pasa por el cable')
 Voltaje = int(input())
 Resistencia = 0.5/Intensidad
 Calculo_seccion = ((0.017*Longitud)/Resistencia)
 print (f'Tu cable necesita una seccion de {Calculo_seccion}')
print ('Calculator made by TheHlb100')

def Potencia_Voltaje():
  print ('Cuanta potencia debe de circular por el cable?')
  Potencia = int(input())
  print ('Cúal es la longitud del cable?')
  Longitud = int(input())
  print ('Cúal es el voltaje que pasa por el cable')
  Voltaje = int(input())
  Intensidad = Potencia/Voltaje
  Resistencia = 0.5/Intensidad
  Calculo_seccion = ((0.017*Longitud)/Resistencia)
  print (f'Tu cable necesita una seccion de {Calculo_seccion}')

def Potencia_Intensidad():
  print ('Cuanta potencia debe de circular por el cable?')
  Potencia = int(input())
  print ('Cúal es la longitud del cable?')
  Longitud = int(input())
  print ('Cúal es la intensidad que pasa por el cable')
  Intensidad = int(input())
  Resistencia = 0.5/Intensidad
  Calculo_seccion = ((0.017*Longitud)/Resistencia)
  print (f'Tu cable necesita una seccion de {Calculo_seccion}')

#INTRODUCCION
print('Bienvenido a la calculadora de la seccion de cable')
print ('Elige entre estas opciones')
print ('Me proporcionan intensidad y voltaje(1)')
print ('Me proporcionan potencia y voltaje (2)')
print ('Me proporcionan intensidad y potencia (3)')
Eleccion = int(input())
if Eleccion == 1:
 Intensidad_Voltaje()
if Eleccion ==2:
  Potencia_Voltaje()
if Eleccion ==3:
  Potencia_Intensidad()

print ('Calculator made by TheHlb100')