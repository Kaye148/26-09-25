import os 
os.system("cls")

pares = 0
impares = 0
soma_pares = 0
soma_impares = 0
soma_geral= 0
contador_geral = 0

while True:
    numeros = int(input("digite um número: "))
    if numeros > 0:
        contador_geral += 1
        soma_geral += numeros
        if numeros % 2 == 0:
            pares +=1
            soma_pares += numeros
        else:impares += 1
    if numeros == 0:
        break
    
#media_pares = soma_pares / pares if pares != 0 else 0
#media_geral = soam_geral / contador_geral if contador_geral != 0 else 0

if pares !=0:
    media_pares = soma_pares / pares
else:
    media_pares = 0

if contador_geral != 0:
    media_geral = soma_geral / contador_geral
else:
    media_geral = 0

print(f"\nquantidade de pares : {pares}")
print(f"quantidade_impares: {impares} ")
print(f"media de numeros pares: {media_pares}")
print(f"media geral: {media_geral}")