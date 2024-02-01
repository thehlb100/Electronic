import math
print("A que distancia estas del altavoz?")
distancia = int (input())
print ("Cúal es la potencia del altavoz en W?")
potencia = int (input())
print ("Cuantos dB hay a un m del altavoz?")
dB = int (input())
resultado_dB = dB - 20*(math.log(potencia,10)) + 10*(math.log(distancia,10))
print(f"A la distancia de = {distancia}  hay unos dB de = {resultado_dB}")
