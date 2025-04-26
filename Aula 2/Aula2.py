# Exmplo 1: CALCULO DE FRETE GRÁTIS
compra = float(input("Qual o valor da sua compra? "))

if compra > 100:
    print("Você ganhou frete grátis!")
else:
    print("Frete: R$20,00")

# Exemplo 2: CLASSIFICAR FAIXA ETÁRIA
    idade = int(input("Qual sua Idade?"))

    if idade < 12:
        print("Criança")
    elif idade < 18:
        print("Adolecente")
    elif idade < 60:
        print("Adulto")
    else:
        print("Idoso")

# Exemplo 3: VERIFICAR HORARIO DE FUNCIONAMENTO
    hora = int(input("Digite a hora atual (0 a 23):"))

    if hora > 9 and hora < 18:
        print("Loja aberta.")
    else:
        print("Loja Fechada.")

# Exemplo 4: TEMPERATURA E CLIMA
temperatura = float(input("Qual a temperatura agora?"))

if temperatura > 30:
    print("Está quente! Use roupas leves.")
elif temperatura > 20:
    print("Clima agradável.")
else:
    print("Está Frio! Vista um casaco.")

# Exemplo 5: VERIFICANDO SE UM NUMERO É PAR / DIVISÍVEL
numero = int(input("Digite um número:"))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é Impar.")