'''Peça um número ao usuário e imprima a tabuada dele de 10 até 1 (ordem decrescente).'''

numero = int(input("Digite um número para ver a tabuada: "))
print(f"\nTabuada do {numero} (de 10 até 1):")
for i in range(10, 0, -1):
   resultado = numero * i
   print(f"{numero} x {i} = {resultado}")