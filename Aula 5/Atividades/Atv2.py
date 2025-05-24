'''2. Peça ao usuário para cadastrar 3 produtos. Para cada produto, informe: nome e
preço.
Guarde essas informações em uma lista. Depois, mostre todos os produtos e seus
preços e a média dos preços'''
produtos = []
for i in range(1, 4):
   print(f"\nCadastro do {i}º produto:")
   nome = input("Digite o nome do produto: ")
   preco = float(input("Digite o preço do produto: "))
   produtos.append({"nome": nome, "preco": preco})
print("\nLista de Produtos:")
soma_precos = 0
for produto in produtos:
   print(f"{produto['nome']}: R$ {produto['preco']:.2f}")
   soma_precos += produto['preco']
media = soma_precos / len(produtos)
print(f"\nMédia dos preços: R$ {media:.2f}")