def converter_celsius_para_fahrenheit():
   """
   Função que converte temperatura de Celsius para Fahrenheit.
   Trata erros se o usuário digitar texto ou valor inválido.
   """
   try:
       celsius = float(input("Digite a temperatura em Celsius: "))
       fahrenheit = (celsius * 9/5) + 32
       print(f"{celsius:.2f}°C equivalem a {fahrenheit:.2f}°F")
   except ValueError:
       print("Erro: Por favor, digite um valor numérico válido.")
   except Exception as e:
       print(f"Ocorreu um erro inesperado: {e}")
# Executa o programa 2
if __name__ == "__main__":
   converter_celsius_para_fahrenheit()