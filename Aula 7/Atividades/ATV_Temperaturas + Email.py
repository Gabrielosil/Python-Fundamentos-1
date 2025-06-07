'''3- Crie uma função chamada main que, dentro de um loop, peça ao usuário para 
escolher  uma  opção.  Use  try  e  except  para  tratar  entradas  inválidas  (não 
numéricas). Se o usuário digitar 1, chame capturar_dados(), se digitar 2, chame 
converter_celsius_para_fahrenheit(),  e  se  digitar  0,  encerre  o  programa.  Para 
números fora do intervalo, exiba uma mensagem de opção inválida.'''

def capturar_dados():
   '''
   Função que captura nome, idade e email do usuário e apresenta no terminal.
   Usa Exception para capturar erros inesperados e valida nome e email.
   '''
   try:
       nome = input("Digite seu nome: ")
       # Validação para não aceitar números no nome
       if not nome.replace(" ", "").isalpha(): # ignora espaços para validação
           print("Erro: O nome não pode conter números ou caracteres especiais.")
           return # Retorna para o menu principal em caso de erro
       idade = int(input("Digite sua idade: "))
       email = input("Digite seu email: ")
       # Validação para aceitar email apenas se tiver '@'
       if "@" not in email:
           print("Erro: O email deve conter o caractere '@'.")
           return # Retorna para o menu principal em caso de erro
       print("\nDados capturados:")
       print(f"Nome: {nome}")
       print(f"Idade: {idade}")
       print(f"Email: {email}")
   except ValueError:
       print("Erro: A idade deve ser um número inteiro válido.")
   except Exception as e:
       print(f"Ocorreu um erro inesperado: {e}")

def converter_celsius_para_fahrenheit():
   '''
   Função que converte temperatura de Celsius para Fahrenheit.
   Trata erros se o usuário digitar texto ou valor inválido.
   '''
   try:
       celsius = float(input("Digite a temperatura em Celsius: "))
       fahrenheit = (celsius * 9/5) + 32
       print(f"{celsius:.2f}°C equivalem a {fahrenheit:.2f}°F")
   except ValueError:
       print("Erro: Por favor, digite um valor numérico válido.")
   except Exception as e:
       print(f"Ocorreu um erro inesperado: {e}")

def main():
   '''
   Função principal que exibe um menu de opções em loop.
   '''
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

# Execução do programa
if __name__ == "__main__":
   main()