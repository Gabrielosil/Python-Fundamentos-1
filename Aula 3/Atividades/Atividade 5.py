'''Crie um programa que calcule e mostre a soma de todos os números ímpares
entre 1 e 100.'''

soma_impares = 0
while True:
   numero = int(input("Digite um número (0 para parar): "))
   if numero == 0:
       break
   if numero % 2 != 0:
       soma_impares += numero
print(f"A soma dos números ímpares digitados é: {soma_impares}")