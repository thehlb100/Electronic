#CALCULADORA LONGITUD ONDAS ELECTROMAGNÉTICAS
print ('Bienvenido a la calculadora de longitud de onda')
print ('Introduce la frecuencia de la que deseas conocer su longitud de onda')

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