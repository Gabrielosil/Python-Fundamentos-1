class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f'{self.nome} está falando')

    def aniversario(self):
        self.idade += 1
        # CORREÇÃO: A f-string deve usar {self.nome} e não (self-nome)
        print(f"{self.nome} fez aniversário e agora tem {self.idade} anos!")

# --- Interação com o usuário ---
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

# --- Criando objetos a partir da classe Pessoa ---
# CORREÇÃO: "pessoal" foi renomeado para "pessoa1" para maior clareza
pessoa1 = Pessoa(nome, idade)
pessoa2 = Pessoa("Gabriela", 19)

# --- Alterando os valores dos atributos ---
pessoa2.nome = "Gabriel"
pessoa2.idade = 20

# --- Executando os métodos da classe ---