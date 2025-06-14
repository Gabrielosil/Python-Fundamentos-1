'''2 - Crie um jogo de Pedra, Papel ou Tesoura, onde o jogador escolhe 
uma  das  três  opções  e  o  computador  escolhe  aleatoriamente.  O  jogo 
deve  mostrar  quem  ganhou  a  rodada.  Depois  de  cada  partida,  o 
programa  deve  perguntar  se  o  jogador  quer  continuar.  O  jogo  só 
termina quando o jogador digitar "não".'''

import random

def jogar():
    """
    Função principal que executa o jogo de Pedra, Papel ou Tesoura.
    """
    opcoes = ["pedra", "papel", "tesoura"]

    while True:
        # --- Escolha do Jogador ---
        # Usamos um loop para garantir que o jogador insira uma opção válida.
        escolha_jogador = ""
        while escolha_jogador not in opcoes:
            escolha_jogador = input("Escolha Pedra, Papel ou Tesoura: ").lower()
            if escolha_jogador not in opcoes:
                print("Opção inválida! Por favor, tente novamente.")

        # --- Escolha do Computador ---
        escolha_computador = random.choice(opcoes)

        # --- Exibe as escolhas ---
        # .capitalize() é usado para deixar a primeira letra maiúscula, melhorando a apresentação.
        print(f"\nSua escolha: {escolha_jogador.capitalize()}")
        print(f"Escolha do computador: {escolha_computador.capitalize()}\n")

        # --- Lógica para determinar o vencedor ---
        if escolha_jogador == escolha_computador:
            print("Resultado: Foi um empate!")
        # Condições em que o jogador ganha
        elif (escolha_jogador == "pedra" and escolha_computador == "tesoura") or \
             (escolha_jogador == "tesoura" and escolha_computador == "papel") or \
             (escolha_jogador == "papel" and escolha_computador == "pedra"):
            print("Resultado: Você ganhou esta rodada!")
        # Se não empatou e o jogador não ganhou, o computador ganhou.
        else:
            print("Resultado: O computador ganhou esta rodada!")

        # --- Pergunta se o jogador quer continuar ---
        print("-" * 30) # Imprime uma linha para separar as rodadas
        continuar = input("Deseja jogar novamente? (Digite 'não' para sair): ").lower()

        # Verifica a resposta e encerra o jogo se for "não".
        # Também verifica "nao" sem o til para facilitar.
        if continuar == "não" or continuar == "nao":
            print("\nObrigado por jogar. Até a próxima!")
            break # Encerra o loop principal
        
        print("\n--- Nova Rodada ---")

# Inicia o jogo chamando a função principal
jogar()