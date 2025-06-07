def dividir():
    try:
        numerador = float(input("Digite o numerador: "))
        denominador = float(input("Digite o denominador: "))
        resultado = numerador / denominador
        print(f"Resultado: {resultado}")
    except ZeroDivisionError:
        print("Erro: divisão por zero não é permitida.")
    except ValueError:
        print("Erro: entrada inválida. Digite números válidos.")

dividir()
