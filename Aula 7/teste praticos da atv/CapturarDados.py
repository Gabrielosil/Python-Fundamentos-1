def capturar_dados():
   """
   Função que captura nome, idade e email do usuário e apresenta no terminal.
   Usa Exception para capturar erros inesperados e valida nome e email.
   """
   try:
       nome = input("Digite seu nome: ")
       # Validação para não aceitar números no nome
       if not nome.replace(" ", "").isalpha(): # ignora espaços para validação
           print("Erro: O nome não pode conter números ou caracteres especiais. Por favor, tente novamente.")
           return # Retorna para permitir uma nova tentativa
       idade = int(input("Digite sua idade: "))
       email = input("Digite seu email: ")
       # Validação para aceitar email apenas se tiver '@'
       if "@" not in email:
           print("Erro: O email deve conter o caractere '@'. Por favor, tente novamente.")
           return # Retorna para permitir uma nova tentativa
       print("\nDados capturados:")
       print(f"Nome: {nome}")
       print(f"Idade: {idade}")
       print(f"Email: {email}")
   except ValueError:
       print("Erro: A idade deve ser um número inteiro válido. Por favor, tente novamente.")
   except Exception as e:
       print(f"Ocorreu um erro inesperado: {e}")
# Executa o programa
if __name__ == "__main__":
   while True: # Adiciona um loop para que o usuário possa tentar novamente
       capturar_dados()
       resposta = input("Deseja capturar novos dados? (s/n): ").lower()
       if resposta != 's':
           break