'''3. Cadastre 4 visitantes de um museu. Para cada um, registre nome e idade. Guarde os
dados em uma lista de tuplas. Depois mostre quem é o visitante mais velho e a média
de idade'''

visitantes = []

for i in range(1, 5):

    print(f"\nCadastro do {i}º visitante:")

    nome = input("Digite o nome do visitante: ")

    idade = int(input("Digite a idade do visitante: "))

    visitantes.append((nome, idade))

print("\nLista de Visitantes:")

soma_idades = 0

mais_velho = visitantes[0]

for nome, idade in visitantes:

    print(f"{nome}: {idade} anos")

    soma_idades += idade

    if idade > mais_velho[1]:

        mais_velho = (nome, idade)

media = soma_idades / len(visitantes)

print(f"\nVisitante mais velho: {mais_velho[0]} com {mais_velho[1]} anos")

print(f"Média de idade: {media:.1f} anos") 