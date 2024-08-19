# Classe conta bancária

class ContaBancaria:
    def __init__(self, numCont, nomePessoa, saldo, tipoConta):
        self.numCont = numCont
        self.nomePessoa = nomePessoa
        self.saldo = saldo
        self.tipoConta = tipoConta

    @property
    def numCont (self):
        return self.__professor
    @numCont.setter
    def numCont(self, numCont):
        self.__numCont = numCont

    @property
    def nomePessoa (self):
        return self.__nomePessoa
    @nomePessoa.setter
    def nomePessoa(self, nomePessoa):
        self.__nomePessoa = nomePessoa

    @property
    def saldo (self):
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo):
        self.__nomePessoa = saldo

    @property
    def tipoConta (self):
        return self.__tipoConta
    @tipoConta.setter
    def tipoConta(self, tipoConta):
        self.__tipoConta = tipoConta

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

<<<<<<< HEAD
# Implementar o exercicio de fixação add:contaBancaria(Cont-1) 

# commit aula 19 de agosto
=======
class ContaCorrente(ContaBancaria):
    def __init__(self,  numCont, nomePessoa, saldo, tipoConta, limite):
        super().__init__(numCont, nomePessoa, saldo, tipoConta)  # Chama o construtor da classe pai para definir idioma e nivel
        self.limite = limite

    @property
    def limite (self):
        return self.__limite
    @limite.setter
    def limite(self, limite):
        if saldo>=limite:
            self.__limite = limite
        else:


class ContaPoupanca(ContaBancaria):
        pass
class ContaInvestimento(ContaBancaria):
        pass
>>>>>>> POD
