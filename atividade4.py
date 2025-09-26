import os
os.system 

while True:
    print("""
codigo   | descrição
 1       |acicionar familia
 2       | sair e exibir resultados  
""")

    opcao = int(input("digite a opção desejada"))
    match opcao:
    case 1:salario = float(input("informe o salario: "))
        
