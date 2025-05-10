'''Crie um programa que calcule e mostre a soma de todos os números ímpares
entre 1 e 100.'''

soma = 0

for i in range(1, 101):
    if i % 2 != 0:
        soma += i

print("A soma dos ímpares de 1 a 100 é:", soma)