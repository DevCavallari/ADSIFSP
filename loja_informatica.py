print("Bem-vindo!")
print("Aqui temos os seguintes estabelecimentos:")
print("1 - Fenix Informatica")
print("2 - Lan House")
print("3 - Escritório de Advocacia")

while True:
    escolha = input("Digite o número correspondente ao local que deseja visitar: ")
    
    if escolha.isdigit():
        escolha = int(escolha)
        if escolha == 1:
            print("A Loja de Informática fica no 1º andar, à esquerda do elevador.")
            break
        elif escolha == 2:
            print("A Lan House fica à esquerda da Fenix.")
            break
        elif escolha == 3:
            print("O Escritório de Advocacia está no 2º andar.")
            break
        else:
            print("Opção inválida. Por favor, digite 1, 2 ou 3.")
    else:
        print("Entrada inválida. Por favor, digite apenas números.")


