# Classe conta bancária

class ContaBancaria:
    def __init__(self, numCont, nomePessoa, saldo, tipoConta):
        self.numCont = numCont
        self.nomePessoa = nomePessoa
        self.saldo = saldo
        self.tipoConta = tipoConta

# 2f indica a formatação em ponto flutuante com duas casas decimais
    def deposito(self, quantidade):
        self.saldo += quantidade
        print(f"Depósito de R${quantidade:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")

    def saque(self, quantidade):
        if quantidade > self.saldo:
            print(f"Saque de R${quantidade:.2f} falhou. Saldo insuficiente: R${self.saldo:.2f}")
        else:
            self.saldo -= quantidade
            print(f"Saque de R${quantidade:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

# Teste de métodos
P1 = ContaBancaria(999, "Felipe", 1000.0, "Conta Corrente")
print(f"Conta: {P1.numCont}, Titular: {P1.nomePessoa}, Tipo: {P1.tipoConta}")

# Exibir saldo inicial
P1.exibir_saldo()

# Realizar um depósito
P1.deposito(500.0)

# Realizar um saque
P1.saque(200.0)

# Tentar realizar um saque maior que o saldo
P1.saque(2000.0)

# Exibir saldo final
P1.exibir_saldo()