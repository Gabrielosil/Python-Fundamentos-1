#sintaxe:
try:
    n = int(input("Digite um número: "))
    resultado = 10 / n
except ValueError:
    print ("Voce nao digitou um numero.")
except ZeroDivisionError:
    print("Divisao por zero nao e permitida.")
else:
    print ("Resultado:", resultado)
finally:
    print("Fim da operação.")