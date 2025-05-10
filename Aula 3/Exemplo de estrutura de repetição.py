# Perguntar a senha até acertar
senha_correta = "python123"
tentativa = ""

while tentativa != senha_correta:
    tentativa = input("Digite a senha: ")

    print("Acesso liberado!")

# Somar vários números até digitar 0

soma = 0
numero = int(input("Digite um número (0 para sair): "))

while numero != 0:
        soma += numero
        numero = int(input("Digite outro número (0 para sair): "))
        print("A soma total é:", soma)

# Contar quantas palavras o usuário digitou

frase =  input("Digite uma frase (ou 'sair' para encerrar): ")
quantidade = 0

while frase != "sair":
        quantidade += len(frase.split())
        frase = input("Digite outra frase (ou 'sair' para encerrar): ")
        print("Você digitou", quantidade, "palavras.")