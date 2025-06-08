import math 
from random import randint

#-----------------------PROGRAMAS------------------------------

#CALCULADORA LONGITUD DE ONDA DE UNA FRECUENCIA
def calculadora_longitud_onda():
  print ('Bienvenido a la calculadora de longitud de onda')
  print ('Introduce la frecuencia de la que deseas conocer su longitud de onda ')

  frecuencia = int(input())

  print ('En que unidad está la frecuencia')
  print ('(1) MHz')
  print ('(2) KHz')
  print ('(3) Hz')

  unidad = int(input())


  if unidad == 1:
    calculo_Longitud = (3*(10**8)/(frecuencia*(10**6)))
    print (f'La longitud de onda es de {calculo_Longitud}m')


  if unidad == 2:
    calculo_Longitud = (3*(10**8)/(frecuencia*(10**3)))
    print (f'La longitud de onda es de {calculo_Longitud}m')

  if unidad == 3:
    calculo_Longitud = (3*(10**8)/(frecuencia))
    print (f'La longitud de onda es de {calculo_Longitud}m')


  print ('Made by theHLB100')

#CALCULADORA TENSIONES ONDA SINOSUIDAL
def calcularondacompleta () :
 pi = 3.14159
 print ("¿Cúal es la tensión en V de la fase 1?")
 Voltajefase1 = int(input())
 print ("¿Cúal es la tensión en V de la fase 2?")
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
 print ("La tensión del diodo es =", Vdiod)

#MULTIPLICADORES DE NÚMEROS (PRUEBAS)
def seleccionmultiplicacion ():
  print ("Cúantos números deseas multiplicar?")
  Select = int(input())
  if Select == 2:
   multiplicaciondosnumeros ()
  if Select == 3:
   multiplicaciontresnumeros ()

def multiplicaciondosnumeros ():
 print ("Cual es el número A?")
 NumeroA = int (input ())
 print ("Cual es el número B?")
 NumeroB = int (input ())
 multiplicacion1 = NumeroA * NumeroB
 print ("El resultado es =", multiplicacion1)
 return multiplicacion1

def multiplicaciontresnumeros ():
 print ("Cual es el número A?")
 NumeroA = int (input ())
 print ("Cual es el número B?")
 NumeroB = int (input ())
 print ("Cual es el número C?")
 NumeroC = int (input())
 multiplicacion1 = NumeroA * NumeroB * NumeroC
 return multiplicacion1

#CALCULADORA PÉRDIDAS EN dB DE SONIDO EMITIDO POR UN ALTAVOZ
def Perdidas_por_distancia():
  print("A que distancia estas del altavoz?")
  distancia = int (input())
  print ("Cúal es la potencia del altavoz en W?")
  potencia = int (input())
  print ("Cuantos dB hay a un metro del altavoz?")
  dB = int (input())
  resultado_dB = dB - 20*(math.log(potencia,10)) + 10*(math.log(distancia,10))
  print(f"A la distancia de = {distancia}m  hay una périda de {resultado_dB}dB")

#CALCULADORA TENSIÓN MÁXIMA Y MÍNIMA DE UNA ONDA SINOSUIDAL A PARTIR DE SU TENSIÓN EFICAZ 
def Calculadora_VoltajeMaximo_VoltajeMínimo():
 print ("Dime el vaLor eficaz")
 pi = 3.14156
 Raiz2 = 1.414
 Vef= int (input ())
 Vmax = Vef * Raiz2
 Vmed = Vmax / pi 

 print ("El valor máximo es =", Vmax)
 print ("El valor medio es =", Vmed)

def calculadoramediaonda():
 pi = 3.141516
 print ("Cual es la tensión de entrada al transformador?")
 Voltajentrada = int(input ())
 print ("Cual es la tensión de salida del transformador?")
 Voltajesalida = int (input ())
 Vmaxin = Voltajentrada * 1.414
 Vmaxs = Voltajesalida*1.414
 Vmed = Vmaxs/pi
 Vmed1 = Vmaxin/pi
 print ("Cual es el valor de la resistencia RL en ohm?")
 Res = int (input())
 Imed = Vmed/Res
 Vmeddiodo= (Vmaxs-0.7)/pi
 Imeddiodo = Vmeddiodo/Res

 print (f"La tensión máxima de entrada es = {Vmaxin}V")
 print (f"La tensión máxima de salida es =  {Vmaxs}V")
 print (f"La tensión media de la saluda es = {Vmed}V")
 print (f"La tensión media de entrada es = {Vmed1}V")
 print (f"La intensidad media de la salida es = {Imed}V")
 print (f"El valor medio del diodo es = {Vmeddiodo}V")
 print (f"La intensidad media del diodo es = {Imeddiodo}A")

#GENERADOR DE IP RANDOM
def ipgenerator ():
 print ("Cual es la clase de Ip que deseas generar?")
 print ("-Da igual (1)")
 print ("-Clase A (2)")
 print ("-Clase B (3)")
 print ("-Clase C (4)")
 clase =int(input())
 Digito2 = randint(1,255)
 Digito3 = randint(1,255)
 Digito4 = randint (1,255)

 if clase ==1:
  Digito1 = randint(1,255)
 if clase==2:
  Digito1 = randint(1,126)
 if clase ==3:
  Digito1 = randint(127,191)
 if clase==4:
  Digito1 = randint(192,220)
 print(f'La ip generada es = {Digito1}.{Digito2}.{Digito3}.{Digito4}')

#CALCULADORA DE TRANSISTORES
def calculadora_transistores():
  print ("Que deseas calcular?")
  print ("-Intensidad del emisor (1)")
  opcion =int (input())
  if opcion ==1:
   print ("Cual es el valor de la intensidad de la base (Ib)")
   Ib = int (input())
   print ("Cual es el valor de la intensidad del colector (Ic)")
   Ic = int (input ())
   Ie = Ib + Ic
   print ("El valor de la intensidad del emisor es =", Ie)
  if opcion ==2:
   print ("Cual es el valor de Vce?")
   Vce = int(input())
   print("Cual es el valor de Vbe?")
   Vcb= int(input())
   Vce = Vce + Vcb
   print ("El valor de Vce es =", Vce)


#CALCULADORA DE SUBREDES NECESARIAS
def calculate_subnet_info():
    used_hosts = int(input("Enter the number of hosts: "))
    used_nets = int(input("Enter the number of networks: "))
    ip = input("Enter the IP address: ")

    results = ""
    

    # Extract the first octet to determine the IP class
    first_octet = int(ip.split('.')[0])

    # Determine the IP class
    ip_class = ""
    if 1 <= first_octet <= 126:
        ip_class = 'A'
    elif 128 <= first_octet <= 191:
        ip_class = 'B'
    elif 192 <= first_octet <= 223:
        ip_class = 'C'
    else:
        return "Invalid IP address. This function only supports Class A, B, and C addresses."

    # Calculate the necessary subnet bits
    total_subnets = 2 ** (math.ceil(math.log2(used_nets)))
    subnet_bits = math.ceil(math.log2(total_subnets))

    # Calculate the necessary host bits
    total_hosts = 2 ** (math.ceil(math.log2(used_hosts + 2)))  # '+ 2' accounts for network and broadcast addresses
    host_bits = math.ceil(math.log2(total_hosts))

    # Determine the default subnet mask based on the IP class
    default_subnet_mask = ""
    if ip_class == 'A':
        default_subnet_mask = '255.0.0.0'
    elif ip_class == 'B':
        default_subnet_mask = '255.255.0.0'
    elif ip_class == 'C':
        default_subnet_mask = '255.255.255.0'

    # Calculate the applied subnet mask based on the number of subnet bits
    binary4 = str('1'*subnet_bits) + ('0'*host_bits) 
    binary = int(binary4)

    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary%10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
   

    # Display the results
    result_string = f"""
        IP Address: {ip}
        IP Class: {ip_class}
        Default Subnet Mask: {default_subnet_mask}
        Applied Subnet Mask: {decimal}
        Subnet Bits: {subnet_bits}
        Host Bits: {host_bits}
    """
    print(result_string)

#CALCULADORA DE IMPEDANCIA EN CIRCUITO RC
def calculadora_Impedancia():
 # CALCULADORA IMPEDANCIA CIRCUITO CONDENSADOR Y RESISTENCIA
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

#CALCULADORA SECCIÓN CABLE
def Calculadora_Seccion_Cable():
 print('Bienvenido a la calculadora de la seccion de cable')
 print ('Elige entre estas opciones')
 print ('Me proporcionan intensidad y voltaje(1)')
 print ('Me proporcionan potencia y voltaje (2)')
 print ('Me proporcionan intensidad y potencia (3)')
 Eleccion = int(input())
 if Eleccion == 1:
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
  
 if Eleccion ==2:
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

 if Eleccion ==3: 
  print ('Cuanta potencia debe de circular por el cable?')
  Potencia = int(input())
  print ('Cúal es la longitud del cable?')
  Longitud = int(input())
  print ('Cúal es la intensidad que pasa por el cable')
  Intensidad = int(input())
  Resistencia = 0.5/Intensidad
  Calculo_seccion = ((0.017*Longitud)/Resistencia)
  print (f'Tu cable necesita una seccion de {Calculo_seccion}')

#NE555
def NE555_MONOESTABLE():
  print ('Cúal es la capacidad del condensador en uF?')
  CapacidadCondensador = int(input())
  print ('Cúal es el valor de R1?')
  Resistencia_1 = int (input())
  Tiempo_Duracion = 1,1*Resistencia_1*CapacidadCondensador
  print(f'EL led durará encendido {Tiempo_Duracion}')

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


#INTRODUCCIÓN
print("thehlb100's calculator")
print(
'''
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMXkolcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccclokXWMMMMMMMMMMMMMM
MMMMMMMMMWk,..',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'..'xNMMMMMMMMMMMMM
MMMMMMMMMO. ,ONWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWN0; .kMMMMMMMMMMMMM
MMMMMMMMMd. oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWd..dWMMMMMMMMMMMM
MMMMMMMMMd. dWMMMMMMWN0OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO0XWMMMMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMMW0c'.....................................................cOWMMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMMO' 'dOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOd, .kWMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMNl .xMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk. cNMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMNc .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO. cNMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMNc .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO. cNMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMNc .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO. cNMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMNc .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO. cNMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMNc .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO. cNMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMWo .oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd. oWMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMMXc..,::::::::::::::::::::::::::::::::::::::::::::::::::,..:KMMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMMMNOo:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:lONMMMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMMMMMMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWMMMMMMMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMMMWXkollllllllllllllllllod0WMMMMMMWKxolllllllllllllllllloxKWMMMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMMNd. .',,,,,,,,,,,,,,,,,...cKMMMXOl. .''''''''''''''''''...oXMMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMWd. cKNWWWWWWWWWWWWWWWWWXd. cXMWo. .lKNNNNNNNNNNNNNNNNNNKl. dWMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMNc .kMMMMMMMMNOxKMMMMMMMMK, ,KMX:  '0MMMMMMMMMMMMMMMMMMMMO. cNMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMNc .kMMMMMMMWk. lNWMMMMMMK, ,KMX:  '0MMMMMMWWWWWWWWMMMMMMO. cNMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMNc .kMMMMW0c;.  .,:xWMMMMK; ,KMX:  '0MMMMWk:;;;;;;:OWMMMMO. cNMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMNc .kMMMMM0oc,  .:lkWMMMMK; ,KMX:  '0MMMMWOlccccccl0WMMMMO. cNMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMNc .kMMMMMMMMO'.dWMMMMMMMK; ,KMX:  '0MMMMMMMMMMMMMMMMMMMMO. cNMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMNc .kMMMMMMMMW00NMMMMMMMMK, ,KMX:  '0MMMMMMMMMMMMMMMMMMMMO. cNMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMWx. ;OXXXXXXXXXXXXXXXXXX0l. lNMWo.. c0XXXXXXXXXXXXXXXXXXO: .dWMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMMNk,.......................oXMMMN0d'......................,xNMMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMMMMN0xddddddddddddddddddxOXWMMMMMMWXOxddddddddddddddddddxONMMMMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMMMMMWWNNNNNNNNNNNNNNNNNNNWMMMMMMMMMMWNNNNNNNNNNNNNNNNNNNNWMMMMMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMMMXx:,''''''''''''''''''';oKWMMMMWKd:'''''''''''''''''''':xXMMMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMMK; .:llllllllllllllllllc. .kWMWOl, .coooooooooooooooooo:. ,0MMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMWo .dWMMMMMMMMMMMMMMMMMMMO' ;XMNc  .kWMMMMMMMMMMMMMMMMMMWx. lNMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMNc .kMMMMMMXO0NWKOKWMMMMMK, ,KMX:  '0MMMMMXkxxxxxxOXMMMMMO. cNMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMNc .kMMMMMWk..,:..lNMMMMMK; ,KMX:  '0MMMMWx'......'kWMMMMO. cNMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMNc .kMMMMMMNl.   ;KMMMMMMK; ,KMX:  '0MMMMMNOkkkkkkONMMMMMO. cNMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMNc .kMMMMMWk'.',..oNMMMMMK; ,KMX:  '0MMMMWx,......,kWMMMMO. cNMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMNc .kMMMMMMKxkXN0x0WMMMMMK; ,KMX:  '0MMMMMKxddddddxKMMMMMO. cNMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMWl .xWMMMMMMMMMMMMMMMMMMM0' ;KMN:  .kMMMMMMMMMMMMMMMMMMMWk. lNMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMM0, .cdxxxxxxxxxxxxxxxxxo, .xWMWkc. 'lxxxxxxxxxxxxxxxxxdl. 'OWMMMWd..dWMMMMMMMMMMMM
MMMMMMMMWd. dWMMMMMKd;....................'l0WMMMWN0l,....................,oKWMMMMWd..dWMMMMMMMMMMMM
MMMMMMMMMd. dWMMMMMMMWXKKKKKKKKKKKKKKKKKKXNMMMMMMMMMMNXKKKKKKKKKKKKKKKKKKXWMMMMMMMWd..dWMMMMMMMMMMMM
MMMMMMMMMd. oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWd .dWMMMMMMMMMMMM
MMMMMMMMM0' 'xKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXk, .OMMMMMMMMMMMMM
MMMMMMMMMWO:........................................................................;kWMMMMMMMMMMMMM
MMMMMMMMMWO:........................................................................;kWMMMMMMMMMMMMM
'''
    )

print ("Que programa deseas ejecutar?")
print ("(1)  Media onda")
print ("(2)  Onda completa")
print ("(3)  Multiplicación dos nºs")
print ("(4)  Calculadora de Vmax y Vef")
print ("(5)  Calculadora de perdidas por distancia en altavoces")
print ("(6)  Generador de IP Random")
print ("(7)  Transformadores")
print ("(8)  Resolvedor de IP")
print ('(9)  Calculadora sección cable')
print ('(10) NE555')
print ('(11) Calculadora pérdidas por distancia (11)')
print ('(12) Calculadora longitud de onda de una frecuencia (12)')
print ('(13) Calculadora de impedancias (13) ')

#SELECCIÓN
Seleccion = int(input())
if Seleccion ==1:
 calculadoramediaonda()
if Seleccion ==2:
 calcularondacompleta()
if Seleccion ==3:
  seleccionmultiplicacion()
if Seleccion ==4:
  Calculadora_VoltajeMaximo_VoltajeMínimo()
if Seleccion ==5:
 Perdidas_por_distancia()
if Seleccion ==6:
 ipgenerator()
if Seleccion ==7:
 calculadora_transistores()
if Seleccion ==8:
 calculate_subnet_info()
if Seleccion ==9:
   Calculadora_Seccion_Cable()
if Seleccion ==10:
  NE555_MONOESTABLE()
if Seleccion ==11:
  Perdidas_por_distancia()
if Seleccion ==12:
  calculadora_longitud_onda()
if Seleccion ==13:
  calculadora_Impedancia()
 




 