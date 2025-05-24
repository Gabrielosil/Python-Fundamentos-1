'''Crie um programa que simule um menu de opções com as seguintes ações:
• Dizer "Olá“
• Dizer a hora (use um print fixo, ex: "São 14:30")
• Sair
O programa deve repetir até o usuário escolher sair.'''

from datetime import datetime

def menu():
    opcoes = [
        ("Dizer 'Olá'", lambda: print("Olá!")),
        ("Dizer a hora", lambda: print(f"São {datetime.now().strftime('%H:%M')}")),
        ("Sair", None)
    ]
    
    while True:
        print("Menu de Opções:")
        for i, (descricao, _) in enumerate(opcoes, start=1):
            print(f"{i}. {descricao}")
        escolha = input("Escolha uma opção (1-3): ")
        
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(opcoes):
                if escolha == 3:
                    print("Saindo do programa. Até mais!")
                    break
                else:
                    acao = opcoes[escolha - 1][1]
                    acao()
            else:
                print("Opção fora do intervalo. Tente novamente.")
        else:
            print("Entrada inválida. Por favor, digite um número.")

menu()
