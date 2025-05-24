'''Peça para o usuário digitar 3 notas.
Armazene em uma lista, calcule e mostre a média com 1 casa decimal.'''

notas = []

for i in range(3):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f"\nA média das notas é: {media:.1f}")
