# EXEMPLO: LISTA DE TAREFAS
class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []
 
    def adicionar_tarefas(self, descricao):
        self.tarefas.append(descricao)
        print("Tarefa adicionada com sucesso!!")
   
    def listar_tarefas(self):
        if not self.tarefas:
            print('Nenhuma tarefa cadastrada no sistema')
        else:
            print('\nLISTA DE TAREFAS:')
            for i, tarefa in enumerate(self.tarefas, start=1):
                print(f'{i}. {tarefa}')
 
    def remover_tarefa(self, numero):
        if 1 <= numero <= len(self.tarefas):
            removida = self.tarefas.pop(numero - 1)
            print(f'Tarefa {removida} foi removida')
        else:
            print('Numero invalido')
 
# CRIANDO UM OBJETO A PARTIR DA CLASSE:
lista = ListaDeTarefas()
 
while True:
    print('''MENU:
          1 - Adicionar Tarefa
          2 - Listar tarefas
          3 - Remover tarefa
          4 - Sair    
''')
   
    opcao = input("Escolha uma opção")
 
    if opcao == "1":
        desc = input("Digite a descrição da tarefa:")
        lista.adicionar_tarefas(desc)
    elif opcao == "2":
        lista.listar_tarefas()
    elif opcao == "3":
        lista.listar_tarefas()
        num = int(input("Digite o numero da tarefa que deseja remover: "))
        lista.remover_tarefa(num)
    elif opcao == 4:
        print("Saindo do programa")
        break
    else:
        print('Opção invalida. Tente novamente')
 