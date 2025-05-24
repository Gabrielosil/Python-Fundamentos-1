'''Crie um programa que:
- Crie uma lista vazia chamada compras.
- Peça ao usuário para digitar 3 itens de mercado.
- Mostre todos os itens ao final.'''

compras = []

for i in range(3):
    item = input(f"Digite o item {i+1} da lista de compras: ")
    compras.append(item)

print("\nItens na lista de compras:")
for item in compras:
    print(f"- {item}")
