import os
os.system

nota = 0
media_aritmetica = 0
quantidade_notas = 0
soma = 0
contador = 0

while True :
    nota = float(input("digite uma nota: "))
    contador +=1
    quantidade_notas +=1
    soma += nota
    resposta = input("deseja inserir mais uma nota ? \nUse S ou N : ").lower()
    if resposta == "n":
        break
    else:
        resposta == "s"
        continue
    print("digite a segunda nota: ")

media = soma / quantidade_notas

print(f"\nMédia: {media}")
