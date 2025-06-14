class Contabancaria:
    def __init__(self, titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f'Deposito de R$ {valor:.2f} realizado')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de {valor:.2f} Realizado')
        else:
            print('Saldo insuficiente')

    def consultar_saldo(self):
        print(f'Saldo atual de {self.titular}: R$ {self.saldo:.2f}')

conta1 = Contabancaria('Gabriel')
conta1.depositar(1000000000)
conta1.sacar(100)
conta1.consultar_saldo()