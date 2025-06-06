alfabeto = ['a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t', 'u', 'v','w','x','y','z']



def criptografa(palavras, chave): 
    criptograf =[]
    for letra in palavras: 
        i= alfabeto.index(letra)
        i_new = (i + chave) % 26
        criptograf.append(alfabeto[i_new])
    return ''.join(criptograf)

def descriptografa(palavras, chave): 
    descriptografa =[]
    for letra in palavras: 
        i= alfabeto.index(letra)
        i_new = (i - chave) % 26
        descriptografa.append(alfabeto[i_new])
    return ''.join(descriptografa)

print("Voce deseja: (1) Criptografar / (2) Descriptografar")
opção = input("Escolha 1 ou 2: ")
palavras = input("Digite uma palavra: ")
chave = int(input("Digite a chave numérica: "))



#if / else
if opção == '1': 
    result = criptografa(palavras,chave)
    print("Palavra criptografada:", result)
elif opção == '2': 
    result = descriptografa(palavras,chave)
    print("Palavra descriptografada:", result)
else: 
    print("Opção invalida.")
