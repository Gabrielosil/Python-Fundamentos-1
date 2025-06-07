def solicitar_idade():
    try:
        idade = int(input("Digite sua idade: "))
        print(f"Idade registrada: {idade} anos")
    except ValueError:
        print("Erro: você deve digitar um número inteiro.")

solicitar_idade()
