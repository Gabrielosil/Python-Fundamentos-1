'''Crie um programa que escolha um número secreto de 1 a 10 (você define
esse número no código). O usuário deverá tentar adivinhar o número. O
programa deve continuar pedindo tentativas até o número correto ser
digitado. Ao final, mostre quantas tentativas foram feitas até o acerto.'''

numero_correto = 7
tentativas = 0
tentativa = -3  
while tentativa != numero_correto:
   tentativa = int(input("Digite a senha: "))
   tentativas += 1

print("Acesso liberado!")
print(f"Você acertou em {tentativas} tentativa(s).")

