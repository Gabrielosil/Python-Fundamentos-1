'''1  -  Crie  um  sistema  de  compras  com  a  classe  Produto.  Cada  produto  tem 
nome  e  preço.  Crie  um  carrinho  (lista)  para  armazenar  os  produtos 
comprados. Mostre um menu em loop para:
• Adicionar produto
• Listar produtos no carrinho
• Calcular total
• Sair'''

class Produto:
    """
    Representa um produto com nome e preço.
    """
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = float(preco)

def adicionar_produto(carrinho):
    """
    Pede ao usuário o nome e o preço de um produto e o adiciona ao carrinho.
    """
    try:
        nome = input("Digite o nome do produto: ")
        preco = input("Digite o preço do produto (ex: 25.50): ")
        produto = Produto(nome, preco)
        carrinho.append(produto)
        print(f"\n✅ Produto '{produto.nome}' adicionado com sucesso!")
    except ValueError:
        print("\n❌ Erro: Preço inválido. Por favor, use um número (ex: 25.50).")

def listar_produtos(carrinho):
    """
    Exibe todos os produtos que estão no carrinho.
    """
    if not carrinho:
        print("\n🛒 O carrinho está vazio.")
        return

    print("\n--- Produtos no Carrinho ---")
    for i, produto in enumerate(carrinho, 1):
        print(f"{i}. {produto.nome} - R$ {produto.preco:.2f}")
    print("----------------------------")

def calcular_total(carrinho):
    """
    Calcula e exibe o valor total dos produtos no carrinho.
    """
    if not carrinho:
        print("\n🛒 O carrinho está vazio. Total: R$ 0.00")
        return

    total = sum(produto.preco for produto in carrinho)
    print(f"\n💰 Valor total do carrinho: R$ {total:.2f}")

def main():
    """
    Função principal que executa o menu do sistema de compras.
    """
    carrinho_de_compras = []
    
    while True:
        print("\n--- Menu do Sistema de Compras ---")
        print("1 - Adicionar produto")
        print("2 - Listar produtos no carrinho")
        print("3 - Calcular total")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_produto(carrinho_de_compras)
        elif opcao == '2':
            listar_produtos(carrinho_de_compras)
        elif opcao == '3':
            calcular_total(carrinho_de_compras)
        elif opcao == '4':
            print("\n👋 Obrigado por usar o sistema. Até logo!")
            break
        else:
            print("\n❌ Opção inválida. Por favor, escolha uma opção de 1 a 4.")

# Executa o programa
if __name__ == "__main__":
    main()