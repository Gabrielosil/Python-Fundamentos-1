from CapturarDados import capturar_dados
from ConversorDeTemperatura import converter_celsius_para_fahrenheit

def main():
    while True:
        print("\nMenu Principal:")
        print("1 - Capturar dados pessoais")
        print("2 - Converter Celsius para Fahrenheit")
        print("0 - Sair")
        try:
            opcao = int(input("Digite sua opção: "))
            if opcao == 1:
                capturar_dados()
            elif opcao == 2:
                converter_celsius_para_fahrenheit()
            elif opcao == 0:
                print("Encerrando o programa...")
                break
            else:
                print("Opção inválida! Digite 1, 2 ou 0.")
        except ValueError:
            print("Erro: Por favor, digite um número válido.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()
