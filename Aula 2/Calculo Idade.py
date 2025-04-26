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