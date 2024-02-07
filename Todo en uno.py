import math 
from random import randint

#PROGRAMAS
def calcularondacompleta () :
 pi = 3.14159
 print ("¿Cúal es el voltaje de la fase 1?")
 Voltajefase1 = int(input())
 print ("¿Cúal es el voltaje de la fase 2?")
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

def Perdidas_por_distancia():
  print("A que distancia estas del altavoz?")
  distancia = int (input())
  print ("Cúal es la potencia del altavoz en W?")
  potencia = int (input())
  print ("Cuantos dB hay a un m del altavoz?")
  dB = int (input())
  resultado_dB = dB - 20*(math.log(potencia,10)) + 10*(math.log(distancia,10))
  print(f"A la distancia de = {distancia}  hay unos dB de = {resultado_dB}")

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

print("Que programa deseas ejecutar?")
print("-Media onda (1)")
print("-Onda completa (2)")
print("-Multiplicación dos nºs (3)")
print("-Calculadora de Vmax y Vef (4)")
print("-Calculadora de perdidas por distancia en altavoces (5)")
print("-Generador de IP Random (6)")
print("-Transformadores(7)")
print("-Resolvedor de IP(8)")

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
