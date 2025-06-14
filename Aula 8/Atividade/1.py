'''1  -  Crie  um  jogo  em  que  o  computador  sorteia  um  número  aleatório 
entre  1  e  10,  e  o  jogador  tenta  adivinhar  qual  é  esse  número.  O 
programa  deve  dizer  se  o  palpite  está  certo  ou  errado.  Após  cada 
rodada,  pergunte  ao  jogador  se  ele  quer  jogar  novamente.  O  jogo 
continua até o jogador digitar "não".'''

import random

def jogar_adivinhacao():
    jogar_novamente = "sim"

    while jogar_novamente.lower() in ["sim", "s"]: # Mudança aqui
        numero_secreto = random.randint(1, 10)
        print("\n--- Jogo de Adivinhação ---")
        print("Tente adivinhar o número secreto entre 1 e 10.")

        try:
            palpite = int(input("Qual é o seu palpite? "))
            if 1 <= palpite <= 10:
                if palpite == numero_secreto:
                    print(f"Parabéns! Você acertou! O número era {numero_secreto}.")
                else:
                    print(f"Que pena! Você errou. O número secreto era {numero_secreto}.")
            else:
                print("Por favor, digite um número entre 1 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

        jogar_novamente = input("Quer jogar novamente? (sim/não): ")

    print("Obrigado por jogar! Até a próxima.")

if __name__ == "__main__":
    jogar_adivinhacao()