'''Peça ao usuário para digitar uma frase e mostre uma palavra por linha.'''

frase = input("Digite uma frase: ")
palavras = frase.split()
print("\nPalavras da frase, uma por linha:")
for palavra in palavras:
   print(palavra)