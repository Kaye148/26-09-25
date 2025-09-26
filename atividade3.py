import os 
os.system("cls")

while True:
    print("""
codigo   | descrição
 1       | Adicionar pessoa
 2       | exibir resultados
 3       | sair
""")
    opcao = int(input("digite a opção desejada: "))
    match opcao:
    case 1:
        idade = int(input("digite seu idade"))
        sexo = input("informe o sexo - use F ou M: ")
        salario = float(input("informe seu slario: "))

        quantidade_salario += 1
        soma_salario += salario
        if idade < menor_idade:
            menor_idade = idade

        if idade > maior_idade:
            maior_idade = idade

        if salario > 5000 and sexo == "F":
            mulheres5k += 1

    case 2:
        media_salarial = soma_salario / quantidade_salarios if quantidade_salarios != 0 else 0
        if menor_idade == 9999:
            menor_idade = 0
        print("\n=Exibindo resultados=")
        print(f"Média de salarios do grupo: {media_salarial}")
        print(f"menor de idade do grupo: {menor_idade}")
        print(f"mairo de idade do grupo: {maior_idade}")
        print(f"quantidade de mulheres com salário acime de 5 mil: {mulheres5k}")
        input("pressione continuar...")
    case 3:
            print("saindo do progrma.")
            input("precione enter para sair...")
            break
    case _:
            print("Opção inválida, tente novamente.")
            input("Pressione enter para continuar...")




