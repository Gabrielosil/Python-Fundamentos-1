'''2 - Crie um jogo de perguntas e respostas (quiz)
Crie  uma  classe  Pergunta  com  enunciado,  lista  de  alternativas  e  a 
resposta correta. Guarde várias perguntas em uma lista. Em cada rodada:
• Sorteie uma pergunta aleatória.
• Mostre as alternativas.
• Peça a resposta do usuário.
• Mostre se ele acertou ou errou e continue até o jogador escolher sair.'''

import random
import os
import time

class Pergunta:
    """
    Representa uma pergunta do quiz com enunciado, alternativas e resposta.
    """
    def __init__(self, enunciado, alternativas, resposta_correta):
        self.enunciado = enunciado
        self.alternativas = alternativas
        self.resposta_correta = resposta_correta

    def mostrar_pergunta(self):
        """
        Exibe o enunciado e as alternativas formatadas.
        """
        print(f"❓ Pergunta: {self.enunciado}\n")
        letras = ['A', 'B', 'C', 'D']
        for i, alternativa in enumerate(self.alternativas):
            print(f"   {letras[i]}) {alternativa}")
        print()

    def checar_resposta(self, resposta_usuario):
        """
        Verifica se a resposta do usuário (A, B, C ou D) corresponde à correta.
        """
        letras = ['A', 'B', 'C', 'D']
        try:
            indice_resposta_usuario = letras.index(resposta_usuario.strip().upper())
            return indice_resposta_usuario == self.resposta_correta
        except ValueError:
            return False

def limpar_tela():
    """Função para limpar o console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """
    Função principal que cria as perguntas e executa o jogo.
    """
    # --- LISTA COMPLETA DE 50 PERGUNTAS ---
    perguntas = [
        # === NÍVEL FÁCIL (1-15) ===
        Pergunta("Qual o nome do estádio do Vasco?", ["Maracanã", "Engenhão", "São Januário", "Laranjeiras"], 2),
        Pergunta("Quem é o maior artilheiro da história do clube?", ["Romário", "Edmundo", "Roberto Dinamite", "Vavá"], 2),
        Pergunta("Qual o principal apelido do clube?", ["Mengão", "Fogão", "Pó de Arroz", "Gigante da Colina"], 3),
        Pergunta("Em que ano o Vasco venceu a Copa Libertadores?", ["1997", "1998", "2000", "1989"], 1),
        Pergunta("Qual animal é o apelido do ídolo Edmundo?", ["Pantera", "Touro", "Leão", "Animal"], 3),
        Pergunta("Qual é o maior rival do Vasco da Gama?", ["Fluminense", "Botafogo", "Flamengo", "Palmeiras"], 2),
        Pergunta("Quais são as cores principais do uniforme do Vasco?", ["Preto e Vermelho", "Preto e Branco", "Branco e Verde", "Azul e Branco"], 1),
        Pergunta("Qual o nome do famoso time vascaíno da década de 1940?", ["Academia de Craques", "Expresso da Vitória", "Máquina Tricolor", "Galácticos da Colina"], 1),
        Pergunta("Qual ídolo era conhecido como 'Reizinho da Colina'?", ["Felipe", "Pedrinho", "Juninho Pernambucano", "Carlos Germano"], 2),
        Pergunta("Qual o esporte que deu origem ao clube?", ["Futebol", "Basquete", "Natação", "Remo"], 3),
        Pergunta("Qual símbolo está no centro da faixa do uniforme do Vasco?", ["Uma âncora", "Uma caravela", "Uma estrela", "A Cruz de Malta"], 3),
        Pergunta("Em que estado brasileiro o Vasco foi fundado?", ["São Paulo", "Bahia", "Minas Gerais", "Rio de Janeiro"], 3),
        Pergunta("Qual destes jogadores foi revelado na base do Vasco?", ["Zico", "Sócrates", "Philippe Coutinho", "Ronaldo Fenômeno"], 2),
        Pergunta("O Vasco foi campeão da Copa do Brasil em que ano?", ["2006", "2008", "2011", "2015"], 2),
        Pergunta("Qual o nome popular do clássico Vasco vs Flamengo?", ["Clássico Vovô", "Clássico dos Gigantes", "Clássico dos Milhões", "Clássico da Amizade"], 2),
        
        # === NÍVEL MÉDIO (16-35) ===
        Pergunta("Quem era o técnico do Vasco na conquista da Libertadores de 1998?", ["Zagallo", "Antônio Lopes", "Joel Santana", "Oswaldo de Oliveira"], 1),
        Pergunta("Contra qual time equatoriano o Vasco decidiu a final da Libertadores de 1998?", ["LDU", "Emelec", "Independiente del Valle", "Barcelona de Guayaquil"], 3),
        Pergunta("Qual jogador marcou o gol do título Brasileiro de 1989 contra o São Paulo?", ["Bismarck", "Sorato", "Bebeto", "William"], 1),
        Pergunta("A famosa 'Resposta Histórica' de 1924 foi uma luta contra qual tipo de preconceito?", ["Xenofobia", "Racismo e preconceito social", "Homofobia", "Intolerância religiosa"], 1),
        Pergunta("Qual foi o adversário do Vasco na final da Copa Mercosul de 2000, conhecida como 'A Virada do Século'?", ["Boca Juniors", "River Plate", "Palmeiras", "Corinthians"], 2),
        Pergunta("Quem era o goleiro titular na conquista da Libertadores de 1998?", ["Fábio", "Hélton", "Carlos Germano", "Fernando Prass"], 2),
        Pergunta("Qual jogador marcou 6 gols em uma única partida no Brasileirão de 1997?", ["Romário", "Viola", "Edmundo", "Evair"], 2),
        Pergunta("Qual destes ídolos foi o capitão da Seleção Brasileira na conquista da Copa do Mundo de 1958?", ["Vavá", "Bellini", "Barbosa", "Ademir de Menezes"], 1),
        Pergunta("Em que ano o Vasco inaugurou o estádio de São Januário?", ["1905", "1927", "1938", "1950"], 1),
        Pergunta("Quem foi o artilheiro do Vasco na campanha da Libertadores de 1998?", ["Donizete", "Luizão", "Ramon", "Pedrinho"], 0),
        Pergunta("Qual jogador fez o famoso gol 'monumental' contra o River Plate na Libertadores 98?", ["Vágner", "Juninho Pernambucano", "Mauro Galvão", "Felipe"], 1),
        Pergunta("Qual o nome do torneio, precursor da Libertadores, vencido pelo Vasco em 1948?", ["Copa Rio", "Campeonato Sul-Americano de Campeões", "Copa Conmebol", "Pequena Taça do Mundo"], 1),
        Pergunta("Qual destes jogadores não foi revelado na base do Vasco?", ["Romário", "Edmundo", "Felipe", "Bebeto"], 3),
        Pergunta("Contra qual time foi a final da Copa do Brasil de 2011?", ["Coritiba", "Avaí", "São Paulo", "Atlético-PR"], 0),
        Pergunta("Qual torneio nacional o Vasco venceu em 2000?", ["Campeonato Brasileiro", "Copa do Brasil", "Copa dos Campeões", "Copa João Havelange"], 3),
        Pergunta("Quem foi o autor do gol do título da Copa Mercosul 2000?", ["Juninho Paulista", "Euller", "Romário", "Jorginho"], 2),
        Pergunta("Qual jogador, ídolo do clube, retornou e encerrou a carreira no Vasco em 2008?", ["Romário", "Edmundo", "Juninho Pernambucano", "Felipe"], 1),
        Pergunta("Qual era o apelido do centroavante artilheiro do Expresso da Vitória, Ademir de Menezes?", ["Animal", "Dinamite", "Queixada", "Pantera"], 2),
        Pergunta("Quem era o presidente do Vasco durante a 'Resposta Histórica'?", ["Eurico Miranda", "Antônio Soares Calçada", "Cyro Aranha", "José Augusto Prestes"], 3),
        Pergunta("Em que cidade foi a final do Sul-Americano de 1948?", ["Montevidéu", "Buenos Aires", "Santiago", "Rio de Janeiro"], 2),
        
        # === NÍVEL DIFÍCIL (36-45) ===
        Pergunta("Qual jogador fez o gol do título Carioca de 1988 sobre o Flamengo, conhecido como 'gol do Cocada'?", ["Romário", "Geovani", "Cocada", "Mazinho"], 2),
        Pergunta("Qual empresa patrocinou o Vasco na vitoriosa campanha de 1997 a 2000?", ["Coca-Cola", "Parmalat", "NationsBank", "ICL"], 2),
        Pergunta("Qual foi o placar agregado da final da Libertadores de 1998 (ida e volta)?", ["2x1", "3x1", "4x1", "5x2"], 2),
        Pergunta("Qual foi o primeiro apelido de Roberto Dinamite, antes de explodir no profissional?", ["Robertinho", "Calu", "Beto", "Garoto do Lins"], 1),
        Pergunta("Contra qual time Edmundo marcou 6 gols no Brasileirão de 1997?", ["Botafogo", "Flamengo", "União São João", "Bahia"], 2),
        Pergunta("Qual destes jogadores não fazia parte do time titular da final da Libertadores de 98?", ["Odvan", "Mauro Galvão", "Válber", "Vágner"], 2),
        Pergunta("Qual foi o último título de Roberto Dinamite pelo Vasco?", ["Brasileirão 1989", "Carioca 1992", "Copa do Brasil 1990", "Carioca 1988"], 1),
        Pergunta("Quem foi o arquiteto que projetou São Januário?", ["Oscar Niemeyer", "Lúcio Costa", "Ricardo Severo", "Affonso Reidy"], 2),
        Pergunta("Além do futebol, em qual outra modalidade o Vasco foi campeão da Liga Nacional em 2000 e 2001?", ["Vôlei", "Futsal", "Polo Aquático", "Basquete"], 3),
        Pergunta("Qual jogador era o capitão do time na conquista da Copa do Brasil de 2011?", ["Fernando Prass", "Dedé", "Juninho Pernambucano", "Alecsandro"], 0),
        
        # === NÍVEL ESPECIALISTA (46-50) ===
        Pergunta("Qual o nome completo do remador português que dá nome ao clube?", ["Vasco da Gama de Portugal", "Vasco de Ataíde da Gama", "Dom Vasco da Gama", "O navegador não dá nome ao clube"], 3),
        Pergunta("Quantos gols Romário marcou na virada histórica da Mercosul 2000?", ["1", "2", "3", "4"], 2),
        Pergunta("Na 'Resposta Histórica', quantos jogadores os rivais exigiam que o Vasco excluísse?", ["7", "10", "12", "15"], 2),
        Pergunta("Qual foi o placar do primeiro jogo da final do Brasileirão de 1997 contra o Palmeiras?", ["1x1", "0x0", "2x1 para o Vasco", "2x1 para o Palmeiras"], 1),
        Pergunta("Quem foi o primeiro presidente da história do Club de Regatas Vasco da Gama?", ["Francisco Gonçalves do Couto Júnior", "Cândido José de Araújo", "Antônio de Almeida Pinho", "Vasco da Gama"], 0),
    ]
    
    # Embaralha a lista de perguntas para garantir que a ordem seja aleatória
    random.shuffle(perguntas)
    
    pontos = 0
    rodada = 1
    
    limpar_tela()
    print("--- BEM-VINDO AO QUIZ DO GIGANTE DA COLINA! (50 PERGUNTAS) ---")
    print("\nTeste seu conhecimento do mais fácil ao mais difícil!")
    print("Prepare-se...")
    time.sleep(4)

    while True:
        # Verifica se todas as perguntas já foram feitas
        if rodada > len(perguntas):
            limpar_tela()
            print("⭐ PARABÉNS, GIGANTE! ⭐")
            print("Você respondeu todas as 50 perguntas do quiz!")
            break
            
        limpar_tela()
        print(f"--- Rodada {rodada}/{len(perguntas)} | Pontuação: {pontos} ---")
        
        # Pega a próxima pergunta da lista embaralhada
        pergunta_atual = perguntas[rodada - 1]
        
        pergunta_atual.mostrar_pergunta()
        
        resposta = input("Digite a sua resposta (A, B, C ou D): ")
        
        if pergunta_atual.checar_resposta(resposta):
            pontos += 1
            print("\n✅ GOOOL! Resposta Correta!")
        else:
            letra_correta = ['A', 'B', 'C', 'D'][pergunta_atual.resposta_correta]
            alternativa_correta = pergunta_atual.alternativas[pergunta_atual.resposta_correta]
            print(f"\n❌ NA TRAVE! A resposta correta era a letra {letra_correta}: '{alternativa_correta}'.")

        print("--------------------------------------------------")
        
        # Pergunta se quer continuar ou sair
        if rodada == len(perguntas):
             print("Pressione ENTER para ver o resultado final...")
             input()
             rodada += 1
        else:
            continuar = input("Pressione ENTER para a próxima pergunta ou digite 'SAIR' para terminar: ").strip().upper()
            if continuar == 'SAIR':
                break
            rodada += 1
            
    limpar_tela()
    print("--- FIM DE JOGO ---")
    print(f"Sua pontuação final foi: {pontos} acertos em {rodada - 1} pergunta(s) respondida(s).")
    print("\nSaudações Vascaínas! Obrigado por jogar! ⚫⚪")

if __name__ == "__main__":
    main()